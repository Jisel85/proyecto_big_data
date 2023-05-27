from typing import Dict

def insertar_info(collection, documento: Dict):
    collection.insert_one(documento)