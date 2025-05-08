from app.schemas.schemas import Master
from app.repository.poke_repository import PokemonRepository
from fastapi import HTTPException

class TrainerRepository:
    def __init__(self):
        self.poke_repository : PokemonRepository = PokemonRepository()
        self.trainers = [] #Es temporal, proximamente se debe conectar a una base

    def get_trainers(self):
        return self.trainers
    
    def get_trainer(self, id : int):
        if id not in range(len(self.trainers)):
            raise HTTPException(status_code=404, detail=f"Trainer not found")
        return self.trainers[id]

    def create_trainer(self, name: str) -> Master:
        #Trae 10 pokemones aleatorios de la 1ra generacion 
        pokemons = self.poke_repository.get_randoms_pokemons()
        trainer = Master(name=name, pokemons=pokemons)
        #Con model dump convertimos clase master a un objeto para agregarlo a trainers
        self.trainers.append(trainer.model_dump())
        return self.trainers[-1]
    
    def update_name_trainer(self, id : int, name : str):
        if id not in range(len(self.trainers)):
            raise HTTPException(status_code=404, detail=f"Trainer not found")
        self.trainers[id]["name"] = name
        return self.trainers[id]
    