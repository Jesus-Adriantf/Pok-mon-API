import requests

url = "https://pokeapi.co/api/v2/pokemon/"

nombre_pokemon = input("Nombre del pokemon: ")

try:
    repuesta = requests.get(url + nombre_pokemon)
    datos = repuesta.json()


    print(f"\n---------- Habilidades de {nombre_pokemon} ----------")
    for abilidad in datos["abilities"]:
        print(abilidad["ability"]["name"])

    print(f"\n---------- Movimientos de {nombre_pokemon} ----------")
    for move in datos["moves"]:
        print(move["move"]["name"])

    print(f"\n---------- Tipo que es {nombre_pokemon} ----------")
    for type in datos["types"]:
        print(type["type"]["name"])

except:
    print(f"No existe este pokemon: {nombre_pokemon}")
