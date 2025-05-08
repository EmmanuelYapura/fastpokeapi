from fastapi import FastAPI
from app.controllers.poke_controllers import service_router
from app.controllers.trainer_controllers import trainer_router

app = FastAPI()
app.include_router(service_router)
app.include_router(trainer_router)
