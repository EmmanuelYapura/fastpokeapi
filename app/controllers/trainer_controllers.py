from fastapi import APIRouter
from app.services.trainer_service import TrainerService

trainer_router = APIRouter(tags=[{"Trainer"}])
trainer_service = TrainerService()

@trainer_router.get('/trainers')
def get_trainers():
    return trainer_service.get_trainers()

@trainer_router.get('/trainers/{id}')
def get_trainer_id(id : int):
    return trainer_service.get_trainer(id)

@trainer_router.post('/trainers')
def create_trainer(name: str):
    return trainer_service.create_trainer(name)

@trainer_router.put('/trainers/{id}')
def update_name_trainer(id : int, name :str):
    return trainer_service.update_name_trainer(id, name)
