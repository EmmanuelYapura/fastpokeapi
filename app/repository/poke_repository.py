from app.clients.pokeapi_client import get_pokemon, create_pokemon
from app.repository.database import pokemons
from app.schemas.schemas import Pokemon
import random

class PokemonRepository:
    def __init__(self):
        try:
            self.pokemons = pokemons
        except Exception as e:
            print(f"Error PokemonRepository: {e}")
            self.pokemons = []
            raise

    #Muestra los 100 pokemones disponibles
    def get_pokemons(self) -> list[dict]:
        return self.pokemons
    
    #Busca un pokemon por id, no todos estan en "database.py"(solo del 0 al 151)
    def get_pokemon_id(self, id : int) -> Pokemon:
        pokemon = get_pokemon(id)
        return create_pokemon(pokemon)
    
    #Retorna 10 pokemones aleatorios
    def get_randoms_pokemons(self):
        pokemons = []
        for i in range(10):
            indice = random.randint(0,150)
            pokemon = self.get_pokemon_id(indice)
            pokemons.append(pokemon)
        return pokemons
