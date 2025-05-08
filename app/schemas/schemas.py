from pydantic import BaseModel

class Pokemon(BaseModel):
    id: int
    name: str
    height: int
    weight: int
    experience: int

class Master(BaseModel):
    name: str
    pokemons: list[Pokemon]
