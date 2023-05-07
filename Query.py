from pymongo import MongoClient

# Connect to MongoDB
mongo_client = MongoClient('mongodb://localhost/pokemon')
mongo_db = mongo_client['pokemondb']
mongo_collection = mongo_db['pokemon_data']

# Query 1: Pokemon named "Pikachu"
print("Query #1 ===============================================================")
query_pikachu = {'name': 'Pikachu'}
results_pikachu = mongo_collection.find(query_pikachu)
for pokemon in results_pikachu:
    print(pokemon)

# Query 2: Pokemon with attack greater than 150
print("Query #2 ===============================================================")
query_attack = {'attack': {'$gt': 150}}
results_attack = mongo_collection.find(query_attack)
for pokemon in results_attack:
    print(pokemon)

# Query 3: Pokemon with ability "Overgrow"
print("Query #3 ===============================================================")
query_overgrow = {'abilities': 'Overgrow'}
results_overgrow = mongo_collection.find(query_overgrow)
for pokemon in results_overgrow:
    print(pokemon)

# Close the connection
mongo_client.close()
