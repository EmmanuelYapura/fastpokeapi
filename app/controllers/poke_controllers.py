from fastapi import APIRouter
from app.services.poke_service import PokemonService

service_router = APIRouter(tags=[{"Pokemon"}]) 
poke_service = PokemonService()

# Trae 151 que representan la 1ra generacion
@service_router.get('/pokemons')
def get_pokemons():
    return poke_service.get_pokemons()

# Busca un pokemon de los 1025 que permite la API 
# Proximamente sera utilizada para que cada entrenador pueda intercambiar un pokemon a eleccion
@service_router.get('/pokemons/{id}')
def get_pokemon(id : int):
    return poke_service.get_pokemon(id)
