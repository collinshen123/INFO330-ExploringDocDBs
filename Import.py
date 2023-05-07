import sqlite3
from pymongo import MongoClient

# Connect to SQLite database
sqlite_conn = sqlite3.connect('pokemon.sqlite')
sqlite_cursor = sqlite_conn.cursor()

# Connect to MongoDB
mongo_client = MongoClient('mongodb://localhost/pokemon')
mongo_db = mongo_client['pokemondb']
mongo_collection = mongo_db['pokemon_data']
mongo_collection.drop()

# Fetch data from SQLite using a join query
query = '''
SELECT p.id, p.name, p.pokedex_number, t.type1, t.type2, p.hp, p.attack, p.defense, p.speed, p.sp_attack, p.sp_defense, a.name as a_name
FROM pokemon p
JOIN pokemon_types_view t ON p.name = t.name
JOIN pokemon_abilities pa ON p.id = pa.pokemon_id
JOIN ability a ON pa.ability_id = a.id
'''
sqlite_cursor.execute(query)
rows = sqlite_cursor.fetchall()

# Map data to MongoDB documents and insert into collection
pokemon_map = {}
for column in rows:
    pokemon_id = column[0]

    if pokemon_id not in pokemon_map:
        pokemon_map[pokemon_id] = {
            '_id': column[0],
            'name': column[1],
            'pokedex_number': column[2],
            'types': [column[3], column[4]],
            'hp': column[5],
            'attack': column[6],
            'defense': column[7],
            'speed': column[8],
            'sp_attack': column[9],
            'sp_defense': column[10],
            'abilities': []
        }

    pokemon_map[pokemon_id]['abilities'].append(column[11])

# Insert documents into MongoDB collection
for pokemon in pokemon_map.values():
    mongo_collection.insert_one(pokemon)
# Fetch table names
sqlite_cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = sqlite_cursor.fetchall()

# Print table names
for table in tables:
    print(table[0])


# Close connections
sqlite_cursor.close()
sqlite_conn.close()
mongo_client.close()
