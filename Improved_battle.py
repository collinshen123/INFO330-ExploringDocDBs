import random
from pymongo import MongoClient

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

def fetch(pokemonid):
    return pokemonColl.find_one({"pokedex_number":pokemonid})

def battle(pokemon1, pokemon2):
    print("Let the Pokemon battle begin! ================")
    print("It's " + pokemon1['name'] + " vs " + pokemon2['name'])

    pokemon1_advantage_counter = 0
    pokemon2_advantage_counter = 0
    for stat in ['hp', 'attack', 'defense', 'speed', 'sp_attack', 'sp_defense']:
        if pokemon1[stat] > pokemon2[stat]:
            print(pokemon1['name'] + " has the advantage in " + stat)
            pokemon1_advantage_counter += 1
        elif pokemon2[stat] > pokemon1[stat]:
            print(pokemon2['name'] + "'s " + stat + " is superior")
            pokemon2_advantage_counter += 1


    # Changed the algorithm to decide a winner based on the number of advantages a certain 
    # pokemon has over the other instead of just using a random number.
    if pokemon1_advantage_counter > pokemon2_advantage_counter:
        winner = 0
    elif pokemon1_advantage_counter < pokemon2_advantage_counter:
        winner = 1
    elif pokemon1['sp_attack'] > pokemon2['sp_attack']:
        winner = 0
    else:
        winner = 1
    
    if winner == 0: print("Battle results: " + pokemon1['name'])
    if winner == 1: print("Battle results: " + pokemon2['name'])

def main():
    # Fetch two pokemon from the MongoDB database
    pokemon1 = fetch(random.randrange(801))
    pokemon2 = fetch(random.randrange(801))

    # Pit them against one another
    battle(pokemon1, pokemon2)

main()
