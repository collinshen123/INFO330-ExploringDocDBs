from pymongo import MongoClient

mongoClient = MongoClient("mongodb://localhost/pokemon.sqlite")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']
print("I found " + pokemonColl.count_documents({}) + " pokemon")
