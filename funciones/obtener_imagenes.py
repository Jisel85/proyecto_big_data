from typing import List
#Importar dependencias requeridas
import fitz
import os
from PIL import Image
import os


def obtener_imagenes(pdf: str) -> List[str]:
    cadena = pdf
    parte1 = cadena.rsplit("\\", 1)[-1]

    # Dividir parte1 desde la derecha en el punto
    parte2 = parte1.rsplit(".", 1)[0]

    # Nombre de la carpeta principal y la subcarpeta
    nombre_carpeta_principal = "images"
    nombre_subcarpeta = parte2

    # Crear la carpeta principal si no existe
    ruta_carpeta_principal = os.path.join(os.getcwd(), nombre_carpeta_principal)
    os.makedirs(ruta_carpeta_principal, exist_ok=True)

    # Crear la subcarpeta dentro de la carpeta principal si no existe
    ruta_subcarpeta = os.path.join(ruta_carpeta_principal, nombre_subcarpeta)
    os.makedirs(ruta_subcarpeta, exist_ok=True)

    #Definir la ruta para las imágenes guardadas
    images_path:  str  = ruta_subcarpeta

    #Abrir archivo PDF
    pdf_file = fitz.open(pdf)

    #Obtener el número de páginas en un archivo PDF
    page_nums = len(pdf_file)

    #Crear una lista vacía para almacenar información de imágenes
    images_list = []

    #Extrae toda la información de las imágenes de cada página.
    for page_num in range(page_nums):
        page_content = pdf_file[page_num]
        images_list.extend(page_content.get_images())

    lista_img= []

    #Guarda todas las imágenes extraídas
    for i, img in enumerate(images_list, start=1):
        #Extrae el número de objeto de la imagen
        xref = img[0]
        #Extraer imagen
        base_image = pdf_file.extract_image(xref)
        #Almacenar bytes de imagen
        image_bytes = base_image['image']
        #Extensión de la imagen de la tienda
        image_ext = base_image['ext']
        #Generar nombre de archivo de imagen
        image_name = str(i) + '.' + image_ext
        lista_img.append(nombre_carpeta_principal + '\\' + nombre_subcarpeta + '\\' + image_name)
        #Guardar imagen
        with open(os.path.join(images_path, image_name) , 'wb') as image_file:
            image_file.write(image_bytes)
            image_file.close()
    return(lista_img)
    


