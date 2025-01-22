# -*- coding: utf-8 -*-
import cv2
from ultralytics import YOLO
import os

# Ruta del modelo entrenado
model_path = "weights/best.pt"

if not os.path.exists(model_path):
    raise FileNotFoundError(f"No se encontró el modelo entrenado en: {model_path}")

model = YOLO(model_path)

# Modificar con la ruta de la imagen que se quiera analizar
image_path = ""

if not os.path.exists(image_path):
    raise FileNotFoundError(f"No se encontró la imagen en: {image_path}")

frame = cv2.imread(image_path)

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

threshold = 0.5

for result in results.boxes.data.tolist():
    x1, y1, x2, y2, score, class_id = result

    if score > threshold:
        cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)

        label = f"Clase: {class_id}, Confianza: {score:.2f}"
        cv2.putText(frame, label, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        care_info = CARE_INFO.get(int(class_id), "Información no disponible")
        print(f"Detectado: Clase {class_id}, Confianza: {score:.2f}")
        print(f"Información de cuidado: {care_info}")

cv2.imshow("Detecciones", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()