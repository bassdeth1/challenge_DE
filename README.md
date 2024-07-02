# Proyecto de Análisis de Rendimiento y Memoria

## Descripción

Este proyecto se encarga de evaluar el rendimiento y uso de memoria de diversas funciones a partir de un conjunto de datos descargado desde Google Drive. El análisis se lleva a cabo mediante scripts en Python que procesan y analizan los datos para ofrecer información valiosa sobre su eficiencia.

## Estructura del Proyecto

- **main.py**: Script principal que coordina la descarga y descompresión de los datos, y ejecuta las funciones de análisis.
- **q1_time.py, q1_memory.py**: Scripts para el análisis del primer conjunto de datos en términos de tiempo y memoria.
- **q2_time.py, q2_memory.py**: Scripts para el análisis del segundo conjunto de datos en términos de tiempo y memoria.
- **q3_time.py, q3_memory.py**: Scripts para el análisis del tercer conjunto de datos en términos de tiempo y memoria.
- **requirements.txt**: Archivo con las dependencias necesarias para ejecutar el proyecto.

## Instalación

Para ejecutar este proyecto, necesitas tener instalado Python 3 y `pip`. Sigue estos pasos para configurar tu entorno:

1. Clona este repositorio en tu máquina local:
    ```sh
    git clone https://github.com/bassdeth1/challenge_DE
    cd challenge_DE
    ```

2. Instala las dependencias del proyecto utilizando `pip`:
    ```sh
    pip install -r requirements.txt
    ```

## Uso

Sigue estos pasos para ejecutar el análisis:

1. Asegúrate de estar en el directorio raíz del proyecto.
2. Ejecuta el script principal:
    ```sh
    python main.py
    ```

Este script descargará los datos necesarios desde Google Drive, los descomprimirá y ejecutará las funciones de análisis, mostrando los resultados en la consola.

## Detalles Técnicos

### main.py

El archivo `main.py` contiene la lógica principal del proyecto. Sus principales funciones son:

- `descargar_y_descomprimir(url, ruta_destino)`: Descarga y descomprime el archivo ZIP desde la URL proporcionada.
- `mostrar_resultados(nombre_funcion, resultados)`: Muestra los resultados obtenidos por cada función de análisis.
- `principal()`: Función principal que coordina la ejecución del proyecto.

### Dependencias

Las dependencias del proyecto se enumeran en el archivo `requirements.txt` e incluyen:
- `memory-profiler==0.61.0`
- `pandas`
- `emoji`
- `gdown`


## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para obtener más detalles.
