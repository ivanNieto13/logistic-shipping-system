import os
import asyncio
import json
import threading
import redis
from celery import Celery, bootsteps
from motor.motor_asyncio import AsyncIOMotorClient


from ...interfaces.schemas.shipment_event import CreateShipmentEvent
from ...application.usecases.shipment_event.integrated_event import IntegratedEventUseCase
from ...infrastructure.database.repositories.shipment_repository import ShipmentRepository
from ...infrastructure.database.repositories.shipment_event_repository import ShipmentEventRepository
from ...infrastructure.config.settings import settings

REDIS_URL = os.getenv("REDIS_URL", settings.REDIS_URL)
CHANNEL_NAME = os.getenv("SHIPMENT_EVENT_CHANNEL", "shipment_event")
MONGO_URI = os.getenv("DATABASE_URL", "mongodb://root:example@db:27017")

app = Celery(
    "event_consumer",
    broker=REDIS_URL,
    backend=REDIS_URL
)

app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
)

class IntegratedEventConsumer(bootsteps.StartStopStep):
    requires = {"celery.worker.components:Timer"}

    def __init__(self, worker, **kwargs) -> None:
        super().__init__(worker, **kwargs)
        self._redis_client = None
        self._pubsub = None
        self._thread = None
        self._stopped = threading.Event()

    def start(self, worker) -> None:
        print(f"Start listening {CHANNEL_NAME} channel events.")
        self._redis_client = redis.from_url(REDIS_URL, decode_responses=True)
        self._pubsub = self._redis_client.pubsub()
        self._pubsub.subscribe(CHANNEL_NAME)
        
        self._thread = threading.Thread(target=self._run_loop, daemon=True)
        self._thread.start()

    def stop(self, worker) -> None:
        print(f"Stop listening {CHANNEL_NAME} channel events.")
        self._stopped.set()
        if self._pubsub:
            self._pubsub.unsubscribe()
            self._pubsub.close()
        if self._redis_client:
            self._redis_client.close()
        if self._thread:
            self._thread.join(timeout=2.0)

    def _run_loop(self) -> None:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        client = AsyncIOMotorClient(MONGO_URI, uuidRepresentation="standard")
        db = client[os.getenv("DATABASE_NAME", "app_db")]
        shipment_repo = ShipmentRepository(db)
        shipment_event_repo = ShipmentEventRepository(db)

        while not self._stopped.is_set():
            try:
                message = self._pubsub.get_message(ignore_subscribe_messages=True, timeout=1.0)
                
                if message and message["type"] == "message":
                    self._process_message(message["data"], shipment_repo, shipment_event_repo, loop)
            except Exception as e:
                print(f"Error at: {e}")
                if not self._stopped.is_set():
                    self._stopped.wait(5.0)
        
        client.close()
        loop.close()

    def _process_message(
        self, 
        data: str, 
        shipment_repo: ShipmentRepository, 
        shipment_event_repo: ShipmentEventRepository, 
        loop: asyncio.AbstractEventLoop,
    ) -> None:
        try:
            payload = json.loads(data)
            print(f"Income event payload: {payload}")
            use_case = IntegratedEventUseCase(shipment_repository=shipment_repo, shipment_event_repository=shipment_event_repo)
            result = loop.run_until_complete(use_case.execute(CreateShipmentEvent(**payload)))
            print(f"Event processed, result: {result}")
            
        except json.JSONDecodeError:
            print(f"Invalid JSON: {data}")

app.steps["worker"].add(IntegratedEventConsumer)