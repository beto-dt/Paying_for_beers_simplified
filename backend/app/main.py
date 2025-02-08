from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.app.interfaces.controllers.order_controller import router

app = FastAPI(
    title="Exercie number #1",
    description="Implementa un endpoint en python para obtener el estado de la orden",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)