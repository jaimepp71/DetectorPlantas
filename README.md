# Plant Detector

## Introduction

The **Plant Detector** is an application designed to identify plant species using a pre-trained model based on YOLO (You Only Look Once). This system can process images and perform quick and accurate detections, facilitating plant classification in various situations. 

## Team Members
- Jaime Padilla Padilla
- Fiorella Capolungo
- Sabas Puig Batalla
- Donato Rinaldi
- Miguel Rodríguez Quintana

---

## Project Structure
The repository is organized as follows:

- **`data/`**: Contains data related to the input for the model.
- **`runs/`**: Stores previous model runs, including results.
- **`src/`**: Main source code folder, including the following files:
  - `DetectorPlantas.py`: Main file that implements the detector logic.
  - `Ejecutable.py`: Code used to generate the executable.
  - `GeneradorAlgoritmoYOLO.py`: Script for configuring and training the YOLO model.
  - `image_rc.py` y `Plantilla.py`: Auxiliary scripts.
- **`weights/`**: Contains the YOLO pre-trained weights, such as `best.pt`.
- **`testdata/`**: Folder with a variety of plant images to test the trained model.
- **`README.md`**: This file, providing details about the project.
- **`requeriments.txt`**: List of dependencies required to run the project.
- **`data.yaml`**: YOLO model configuration file.

> **Note:** Due to the large size of the `/data` directory, it is available as a downloadable compressed file at the following link:
```plaintext
   https://upm365-my.sharepoint.com/:u:/g/personal/jaime_padilla_alumnos_upm_es/EZeKEN932NNMvo0fmTVM1hUBM6K-UH87eoONl2YC9ZZAhA?e=98Xr5W
   ```
---

## How to Download the Executable

The project executable is available in the **Releases** section of the GitHub repository. Follow these steps to download it:

1. Go to the GitHub repository.
2. Click on the **Releases** tab at the top of the repository.
   
   ![Imagen de la pestaña Releases](/img/release.png)
   
3. In the list of releases, select the latest version (marked as "Latest").
4. Download the compressed file containing the executable (`PlantDetector_v1.0.zip`).
5. Extract the contents of the downloaded file and run `main.exe`.

> **Note:** The compressed file also contains the `testdata/` directory, which includes a collection of plant images that can be used for quick testing and validation of the trained model.
