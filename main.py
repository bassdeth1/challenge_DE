import zipfile
import os
from typing import List, Tuple
from src.q1_time import q1_time
from src.q1_memory import q1_memory
from src.q2_time import q2_time
from src.q2_memory import q2_memory
from src.q3_time import q3_time
from src.q3_memory import q3_memory
import gdown

def descargar_y_descomprimir(url, ruta_destino):
    # Descargar el archivo ZIP desde Google Drive
    local_filename = os.path.join(ruta_destino, 'tweets.zip')
    os.makedirs(ruta_destino, exist_ok=True)
    gdown.download(url, local_filename, quiet=False)
    # Descomprimir el archivo ZIP
    with zipfile.ZipFile(local_filename, 'r') as zip_ref:
        zip_ref.extractall(ruta_destino)
    # Devolver la ruta del archivo JSON descomprimido
    for file_name in os.listdir(ruta_destino):
        if file_name.endswith(".json"):
            return os.path.join(ruta_destino, file_name)
    return None

def mostrar_resultados(nombre_funcion: str, resultados: List[Tuple]):
    # Mostrar los resultados según la función ejecutada
    if nombre_funcion == "q1_time":
        print(f"Resultados para q1_time: {resultados}")
    elif nombre_funcion == "q1_memory":
        print(f"Resultados para q1_memory: {resultados}")
    elif nombre_funcion == "q2_time":
        print(f"Resultados para q2_time: {resultados}")
    elif nombre_funcion == "q2_memory":
        print(f"Resultados para q2_memory: {resultados}")
    elif nombre_funcion == "q3_time":
        print(f"Resultados para q3_time: {resultados}")
    elif nombre_funcion == "q3_memory":
        print(f"Resultados para q3_memory: {resultados}")

def principal():
    # URL del archivo ZIP a descargar
    url = 'https://drive.google.com/uc?id=1ig2ngoXFTxP5Pa8muXo02mDTFexZzsis'
    ruta_destino = 'archivo/'
    print("Descargando y descomprimiendo el archivo ZIP...")
    archivo_json = descargar_y_descomprimir(url, ruta_destino)
    if archivo_json is None:
        print("No se encontró un archivo JSON en el ZIP.")
        return

    # Ejecutar cada función y mostrar sus resultados
    for func in [q1_time, q1_memory, q2_time, q2_memory, q3_time, q3_memory]:
        nombre_funcion = func.__name__
        result = func(archivo_json)
        mostrar_resultados(nombre_funcion, result)

if __name__ == "__main__":
    principal()
