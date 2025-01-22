from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
from Plantilla import Ui_MainWindow
from ultralytics import YOLO
import cv2

model_path = "weights/best.pt"
model = YOLO(model_path)

CARE_INFO = {
    0: "Aloe Vera:Requiere luz indirecta brillante y riego moderado.",
    1: "Anthurium:Prefiere luz indirecta y un ambiente húmedo.",
    2: "Areca Palm:Necesita luz brillante filtrada y riego constante.",
    3: "Asparagus Fern:Crece mejor con luz indirecta y suelo ligeramente húmedo.",
    4: "Bellflower:Demanda luz brillante y riego moderado.",
    5: "Bird of Paradise:Necesita luz brillante y riego regular.",
    6: "Calathea:Se desarrolla con luz indirecta baja y alta humedad.",
    7: "Calendula:Requiere luz directa y riego moderado.",
    8: "Tulip:Necesita luz brillante y riego regular mientras florece.",
    9: "Water Lily:Debe plantarse en agua y tener luz brillante."
}

class PlantDetectionApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.selected_image_path = None

        self.ui.Seleccionar.clicked.connect(self.select_image)
        self.ui.Analizar.clicked.connect(self.process_image)

    def select_image(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Selecciona una imagen", "", "Archivos de imagen (*.jpg *.jpeg *.png);;Todos los archivos (*)", options=options
        )
        if file_path:
            self.selected_image_path = file_path
            self.display_image(file_path)
            self.ui.Nombre_planta.setText("")
            self.ui.Confianza.setText("")
            self.ui.Caracteristicas.setText("")

    def display_image(self, image_path):
        pixmap = QPixmap(image_path)
        pixmap = pixmap.scaled(
            self.ui.Imagen_planta.width(),
            self.ui.Imagen_planta.height(),
            Qt.KeepAspectRatioByExpanding
        )
        self.ui.Imagen_planta.setPixmap(pixmap)

    def process_image(self):
        if not self.selected_image_path:
            QMessageBox.critical(self, "Error", "Por favor, selecciona una imagen primero.")
            return

        frame = cv2.imread(self.selected_image_path)
        results = model(frame)[0]

        self.ui.Nombre_planta.setText("")
        self.ui.Confianza.setText("")
        self.ui.Caracteristicas.setText("")

        for result in results.boxes.data.tolist():
            x1, y1, x2, y2, score, class_id = result
            if score > 0.2:
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                plant_name = CARE_INFO.get(int(class_id), "Desconocida").split(":")[0]
                care_info = CARE_INFO.get(int(class_id), "Información no disponible").split(":")[1]

                self.ui.Nombre_planta.setText(plant_name)
                self.ui.Confianza.setText(f"Confianza: {score:.2f}")
                self.ui.Caracteristicas.setText(care_info)
                break

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        height, width, channel = frame.shape
        qimage = QImage(frame.data, width, height, channel * width, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qimage)
        pixmap = pixmap.scaled(
            self.ui.Imagen_planta.width(),
            self.ui.Imagen_planta.height(),
            Qt.KeepAspectRatioByExpanding
        )
        self.ui.Imagen_planta.setPixmap(pixmap)

    def resizeEvent(self, event):
        """Ajustar la imagen al tamaño del QLabel al redimensionar la ventana."""
        if self.selected_image_path:
            self.display_image(self.selected_image_path)
        super().resizeEvent(event)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = PlantDetectionApp()
    window.show()
    sys.exit(app.exec_())