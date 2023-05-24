import pytesseract
from typing import List
from PIL import Image
import re
import os

from funciones.lista_pdfs import lista_pdfs
carpeta_pdfs: str  = '.\DatasetTotal'
pdfs: List[str] = lista_pdfs(carpeta_pdfs)
print(pdfs)

def extraer_texto(lista_imagenes: List[str]) -> str:
    """ Extracts the text from a PDF file encoded in base64 and returns the
    number of pages and extracted text.
    If this method cannot extract text, god forbid, it returns an empty string.

    param: base64 text str
    return: extracted text , str
    """
    final_text = []
    
    for imagen_path in lista_imagenes:
        try:
            path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
            pytesseract.pytesseract.tesseract_cmd = path_to_tesseract

            with Image.open(imagen_path) as img:
                texto_imagen = pytesseract.image_to_string(img)
                final_text.append(texto_imagen)

        except (TypeError, FileNotFoundError) as err:
            print(err)

    # Convertir la lista de textos en una cadena de texto
    texto_completo = ' '.join(final_text)
    texto_completo = replacement(texto_completo)

    return texto_completo


def replacement(text: str) -> str:
    """ Replaces some undesired chars, words or sequences on the text.
    Converts to lower case string.

    param: original text
    return: clean text
    """
    # Eliminate white space
    text = text.replace('\t', ' ')
    text = text.replace('\n', ' ')

    return text


def regex(text: str) -> str:
    regex = '\sBigData'
    f1 = re.findall(regex, text)

    if f1 == []:
        return 'No'
    else:
        return 'Si'

