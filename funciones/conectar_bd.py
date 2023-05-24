import os
from pymongo import MongoClient

def conectar_bd():
    connection_str = os.getenv('CREDENCIALES_BD')
    client = MongoClient(connection_str)
    print(client.server_info())
    return client