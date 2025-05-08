from app.repository.trainer_repository import TrainerRepository

class TrainerService:
    def __init__(self):
        self.trainer_service : TrainerRepository = TrainerRepository()

    def get_trainers(self):
        return self.trainer_service.get_trainers()
    
    def get_trainer(self, id : int):
        return self.trainer_service.get_trainer(id)
    
    def create_trainer(self, name : str):
        return self.trainer_service.create_trainer(name)
    
    def update_name_trainer(self, id: int, name: str):
        return self.trainer_service.update_name_trainer(id, name)
    
#FALTA CREAR LOS CONTROLLERS, Y QUE EL MAIN QUEDE SIMPLE
