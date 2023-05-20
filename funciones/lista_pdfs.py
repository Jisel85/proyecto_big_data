import os
from typing import List


def ls(carpeta: str) -> List[str]:
    return os.listdir(carpeta)

def lista_pdfs(carpeta_pdfs: str) -> List[str]:
    lista = []
    for year in ls(carpeta_pdfs):
        for pdf in ls(carpeta_pdfs +'\\' + year):
            lista.append(carpeta_pdfs +'\\' + year + '\\' + pdf)
    return lista
