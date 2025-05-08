from fastapi import HTTPException
import requests
from app.schemas.schemas import Pokemon

def get_all_pokemons(url = 'https://pokeapi.co/api/v2/pokemon?limit=151&offset=0'):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            pokemons = response.json()
            return pokemons["results"]
        else:
            raise HTTPException(status_code=404, detail=f"Pokemons not found")

    except requests.RequestException as e:
        raise HTTPException(status_code=503, detail=f"Error fetching pokemon detail: {e}")
    
def get_pokemon(id: int):
    try:
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{id}/")
        if response.status_code == 200:
            pokemon = response.json()
            return pokemon
        else:
            raise HTTPException(status_code=404, detail=f"Pokemon not found")
    except requests.RequestException as e:
        raise HTTPException(status_code=503, detail=f"Error fetching pokemon detail: {e}")

# Extrae datos a eleccion
def create_pokemon(pokemon : Pokemon):
    details_pokemon = {
        "id": pokemon["id"],
        "name": pokemon["name"],
        "height": pokemon["height"],
        "weight": pokemon["weight"],
        "experience": pokemon["base_experience"]
    }
    return details_pokemon
