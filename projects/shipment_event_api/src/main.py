"""shipment_event_api - FastAPI Application"""
from contextlib import asynccontextmanager
from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .interfaces.api.dependencies import get_redis_adapter

from .infrastructure.config.settings import settings
from .interfaces.api.v1.routes import shipment_event

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Verificar conexión si es necesario
    yield
    # Shutdown: Cerrar conexión a Redis limpiamente
    adapter = get_redis_adapter()
    await adapter.close()

app = FastAPI(
    title="shipment_event_api",
    description="Shipment Event API",
    version="1.0.0",
    debug=settings.DEBUG,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

v1_router = APIRouter(prefix="/v1")
v1_router.include_router(shipment_event.router)

api_router = APIRouter(prefix="/api")
api_router.include_router(v1_router)

app.include_router(api_router)

@app.get("/")
async def root():
    return {
        "message": "Welcome to shipment_event_api",
        "docs": "/docs"
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
