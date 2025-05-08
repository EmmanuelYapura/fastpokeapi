from app.repository.poke_repository import PokemonRepository

class PokemonService:
    def __init__(self):
        self.poke_repository : PokemonRepository = PokemonRepository()

    def get_pokemons(self):
        return self.poke_repository.get_pokemons()
    
    def get_pokemon(self, id : int):
        return self.poke_repository.get_pokemon_id(id)
    
    def get_randoms_pokemons(self):
        return self.poke_repository.get_randoms_pokemons()