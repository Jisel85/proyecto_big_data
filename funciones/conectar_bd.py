import os
from pymongo import MongoClient

def conectar_bd():
    connection_str = os.getenv('CREDENCIALES_BD')
    client = MongoClient(connection_str)
    db = client["proyecto"]
    collection = db["sentencias"]
    print(client.server_info())
    collection.create_index([("Texto", "text")])
    return collection