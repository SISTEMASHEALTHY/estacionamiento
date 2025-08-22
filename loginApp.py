from PySide6.QtWidgets import QDialog
from loginUI import Ui_Dialog
from PySide6.QtWidgets import QMessageBox
from Funciones import validacion_loggin


class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.user_data = None  # aquí guardaremos el resultado

        # Conectar el botón
        self.ui.pushButton.clicked.connect(self.login)

    def login(self):
        usuario = self.ui.lineEdit.text().strip()   # lo que escribió en usuario
        password = self.ui.lineEdit_2.text().strip() # lo que escribió en contraseña

        # 👉 Aquí llamas a tu procedimiento real (ejemplo simulado)
        respuesta= validacion_loggin(usuario, password)
        print(respuesta)

        if respuesta["rol"] == "admin" and respuesta["valido"] == True:
            self.user_data = {"usuario": usuario, "id_usuario": respuesta["id_usuario"], "rol": respuesta["rol"], "valido": respuesta["valido"]}
            self.accept()
        elif respuesta["rol"] == "empleado" and respuesta["valido"] == True:
            self.user_data = {"usuario": usuario, "id_usuario": respuesta["id_usuario"], "rol": respuesta["rol"], "valido": respuesta["valido"]}
            self.accept()

        elif respuesta["Mensaje"]:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Critical)  # Icono de error
            msg.setWindowTitle("Error")
            msg.setText(respuesta["Mensaje"])
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()

        else:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Critical)  # Icono de error
            msg.setWindowTitle("Error")
            msg.setText("Usuario o contraseña incorrectas")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()