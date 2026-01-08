"""shipment_api - FastAPI Application"""
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .interfaces.api.dependencies import get_redis_adapter

from .infrastructure.config.settings import settings
from .interfaces.api.v1.routes import shipment

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Verificar conexión si es necesario
    yield
    # Shutdown: Cerrar conexión a Redis limpiamente
    adapter = get_redis_adapter()
    await adapter.close()

app = FastAPI(
    title="shipment_api",
    description="API built with Clean Architecture",
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

app.include_router(shipment.router, prefix="/api/v1")

@app.get("/")
async def root():
    return {
        "message": "Welcome to shipment_api",
        "docs": "/docs"
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
