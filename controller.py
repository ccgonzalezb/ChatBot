# controller.py
from PyQt5.QtWidgets import QWidget
from model import ChatbotModel
from view import Ui_Form

class ChatbotController(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.model = ChatbotModel()

        # Conectar botón
        self.ui.pushButton.clicked.connect(self.procesar_mensaje)
        # Conectar enter
        self.ui.lineEdit.returnPressed.connect(self.procesar_mensaje)

    def iniciar(self):
        self.view.show()

    def procesar_mensaje(self):
        entrada = self.ui.lineEdit.text()
        if entrada:
            respuesta = self.model.responder(entrada)

            # Mostrar en el chat
            self.ui.textBrowser.append(f"Tú: {entrada}")
            self.ui.textBrowser.append(f"Bot: {respuesta}\n")

            # Limpiar campo de entrada
            self.ui.lineEdit.clear()
