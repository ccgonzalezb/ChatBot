# main.py
import sys
import os
from PyQt5.QtWidgets import QApplication
from controller import ChatbotController

def resource_path(relative_path):
    """Obtiene la ruta correcta ya sea desde .py o desde .exe"""
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    ruta_estilo = resource_path("estilos.qss")
    with open(ruta_estilo, "r") as f:
        app.setStyleSheet(f.read())

    ventana = ChatbotController()
    ventana.show()
    sys.exit(app.exec())