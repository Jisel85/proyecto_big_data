from dotenv import load_dotenv
from typing import List, Dict
from funciones.lista_pdfs import lista_pdfs
from funciones.conectar_bd import conectar_bd
from funciones.obtener_imagenes import obtener_imagenes
from funciones.extraer_texto import extraer_texto
from funciones.crear_dict import crear_dict
from funciones.insertar_info import insertar_info
from concurrent import futures

load_dotenv()

conexion = conectar_bd()

carpeta_pdfs: str = '.\DatasetTotal'
pdfs: List[str] = lista_pdfs(carpeta_pdfs)
print(pdfs)

def procesar_pdf(pdf: str):
    lista_imagenes: List[str] = obtener_imagenes(pdf)
    texto_sentencia: str = extraer_texto(lista_imagenes)
    documento: Dict = crear_dict(texto_sentencia, pdf)
    insertar_info(conexion, documento)

with futures.ThreadPoolExecutor() as execuor: 
    resultados = execuor.map(procesar_pdf, pdfs)
