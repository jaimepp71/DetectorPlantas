# -*- coding: utf-8 -*-
import os
import cv2
import shutil
from ultralytics import YOLO

# Modificar con la ruta de todas las dependencias para lanzar
ROOT_DIR = "."

if not os.path.exists(ROOT_DIR):
    raise FileNotFoundError(f"La ruta {ROOT_DIR} no existe. Asegúrate de que es correcta.")

model = YOLO("yolov8n.yaml")

data_yaml_path = os.path.join(ROOT_DIR, "data.yaml")

if not os.path.exists(data_yaml_path):
    raise FileNotFoundError(f"El archivo data.yaml no se encuentra en {data_yaml_path}.")

results = model.train(data=data_yaml_path, imgsz=416, epochs=30, batch=16, workers=2)

output_dir = os.path.join(ROOT_DIR, "/data/output")

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

shutil.copytree("runs", output_dir, dirs_exist_ok=True)

model_path = os.path.join(output_dir, "Incluir la ruta donde se encuentre el modelo creado")

if not os.path.exists(model_path):
    raise FileNotFoundError(f"El modelo entrenado no se encuentra en {model_path}.")

model = YOLO(model_path)

IMAGES_DIR = os.path.join(ROOT_DIR, "data/test/images")

# Modificar con la ruta de la imagen que queramos utilizar para comprobar el algoritmo creado
IMAGES_NAME = ""

image_path = os.path.join(IMAGES_DIR, IMAGES_NAME)

if not os.path.exists(image_path):
    raise FileNotFoundError(f"La imagen no se encuentra en {image_path}.")

frame = cv2.imread(image_path)

H, W, _ = frame.shape

threshold = 0.5

results = model(frame)[0]

CARE_INFO = {
    0: "Aloe Vera: Requiere luz indirecta brillante y riego moderado.",
    1: "Anthurium: Prefiere luz indirecta y un ambiente húmedo.",
    2: "Areca Palm: Necesita luz brillante filtrada y riego constante.",
    3: "Asparagus Fern: Crece mejor con luz indirecta y suelo ligeramente húmedo.",
    4: "Bellflower: Demanda luz brillante y riego moderado.",
    5: "Bird of Paradise: Necesita luz brillante y riego regular.",
    6: "Calathea: Se desarrolla con luz indirecta baja y alta humedad.",
    7: "Calendula: Requiere luz directa y riego moderado.",
    8: "Tulip: Necesita luz brillante y riego regular mientras florece.",
    9: "Water Lily: Debe plantarse en agua y tener luz brillante."
}

COLORS = {
    0: (0, 255, 0),
    1: (255, 0, 0),
    2: (0, 0, 255),
    3: (255, 255, 0),
    4: (255, 0, 255),
    5: (0, 255, 255),
    6: (128, 0, 128),
    7: (255, 165, 0),
    8: (75, 0, 130),
    9: (0, 128, 128)
}

for result in results.boxes.data.tolist():
    x1, y1, x2, y2, score, class_id = result

    if score > threshold:
        color = COLORS.get(int(class_id), (255, 255, 255))
        cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), color, 2)

        label = results.names[int(class_id)] if int(class_id) in results.names else f"Clase {int(class_id)}"

        cv2.putText(frame, label, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

        care_message = CARE_INFO.get(int(class_id), "No hay información disponible para esta clase.")
        print(f"Detectada: {label} - {care_message}")

scaled_frame = cv2.resize(frame, (640, 640))

cv2.imshow("Resultados", scaled_frame)
cv2.waitKey(0)
cv2.destroyAllWindows()