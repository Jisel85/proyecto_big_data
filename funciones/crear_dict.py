from typing import Dict
from datetime import datetime

def crear_dict(texto_sentencia: str, pdf: str) -> Dict:
    cadena = pdf
    nombre_sentencia_pdf = cadena.rsplit("\\", 1)[-1]

    # Dividir parte1 desde la derecha en el punto
    nombre_sentencia = nombre_sentencia_pdf.rsplit(".", 1)[0]

    #accede al primer carácter de la cadena
    primera_letra = nombre_sentencia[0]
    if primera_letra == 'A':
        primera_letra = 'Auto'
    elif primera_letra == 'C':
        primera_letra = 'Constitucional'
    elif primera_letra == 'T':
        primera_letra = 'Tutela'
    else:
        primera_letra = 'Otra'

    #Captura año de la sentencia desde la carpeta a la que pertenece
    ultimos_dos_caracteres = cadena.split('\\')[2]

    #fecha actual
    fecha_actual = datetime.now()
    fecha_formateada = fecha_actual.strftime("%Y-%m-%d")

    dict_mongo = {
        "Providencia": nombre_sentencia,
        "Tipo": primera_letra,
        "AnoPublicacion" : ultimos_dos_caracteres,
        "Texto": texto_sentencia,
        "FechaPublicacion": fecha_formateada
    }

    return dict_mongo


print(crear_dict("Angela Vargas",".\\DatasetTotal\\2023\\C-065-21.pdf"))