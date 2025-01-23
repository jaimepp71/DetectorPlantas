# Detector de Plantas

## Introducción

El **Detector de Plantas** es una aplicación diseñada para identificar especies de plantas utilizando un modelo preentrenado basado en YOLO (You Only Look Once). Este sistema es capaz de procesar imágenes y realizar detecciones rápidas y precisas, facilitando la clasificación de plantas en diversas situaciones. 

El proyecto incluye código fuente bien estructurado y documentado, así como un ejecutable listo para ser utilizado, que se encuentra disponible en la sección de Releases del repositorio.


## Integrantes
- Jaime Padilla Padilla
- Fiorella Capolungo
- Sabas Puig Batalla
- Donato Rinaldi
- Miguel Rodríguez Quintana

---

## Descripción del Proyecto

---

## Estructura del Proyecto
El repositorio está organizado de la siguiente manera:

- **`data/`**: Contiene información relacionada con los datos de entrada para el modelo.
- **`runs/`**: Almacena las ejecuciones previas del modelo, incluyendo resultados.
- **`src/`**: Carpeta principal del código fuente, que incluye los siguientes archivos:
  - `DetectorPlantas.py`: Archivo principal que implementa la lógica del detector.
  - `Ejecutable.py`: Código usado para generar el ejecutable.
  - `GeneradorAlgoritmoYOLO.py`: Script para configurar y entrenar el modelo YOLO.
  - `image_rc.py` y `Plantilla.py`: Scripts auxiliares.
- **`weights/`**: Contiene los pesos preentrenados del modelo YOLO, como `best.pt`.
- **`testdata/`**: Carpeta con una variedad de imágenes de plantas que puedes usar para probar el modelo ya entrenado.
- **`README.md`**: Este archivo, que proporciona detalles sobre el proyecto.
- **`requeriments.txt`**: Lista de dependencias necesarias para ejecutar el proyecto.
- **`data.yaml`**: Archivo de configuración del modelo YOLO.

---

## Cómo Descargar el Ejecutable

El ejecutable del proyecto se encuentra en la sección de **Releases** del repositorio de GitHub. Sigue estos pasos para descargarlo:

1. Accede al repositorio de GitHub.
2. Haz clic en la pestaña **Releases**, ubicada en la parte superior del repositorio.
   ![Imagen de la pestaña Releases](/img/release.png)
3. En la lista de releases, selecciona la versión más reciente (marcada como "Latest").
4. Descarga el archivo comprimido que contiene el ejecutable (por ejemplo, `DetectorPlantas_v1.0.zip`).
5. Extrae el contenido del archivo descargado y ejecuta `main.exe`.

> **Nota:** El comprimido contiene a su vez el directorio `testdata/`, donde se encuentra una colección de imágenes de plantas que pueden utilizarse para realizar pruebas rápidas y validar el modelo entrenado.
---

## Instalación y Uso

### Requisitos Previos
Antes de ejecutar el proyecto, asegúrate de tener instaladas las siguientes dependencias:

- Python 3.8 o superior
- Las bibliotecas especificadas en `requeriments.txt` (puedes instalarlas ejecutando `pip install -r requeriments.txt`).

### Ejecución del Código Fuente
Para ejecutar el código fuente directamente:

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu_usuario/DetectorPlantas.git
   cd DetectorPlantas
   ```
2. Instala las dependencias:
   ```bash
   pip install -r requeriments.txt
   ```
3. Descarga la carpeta `data` necesaria para entrenar el modelo manualmente desde la siguiente URL y colócala en la raíz del proyecto:
   ```plaintext
   https://upm365-my.sharepoint.com/:u:/g/personal/jaime_padilla_alumnos_upm_es/EZeKEN932NNMvo0fmTVM1hUBM6K-UH87eoONl2YC9ZZAhA?e=98Xr5W
   ```
4. Ejecuta el script principal:
   ```bash
   python src/DetectorPlantas.py
   ```
