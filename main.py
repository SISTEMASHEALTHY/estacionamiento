import sys
from PySide6.QtWidgets import QApplication
from loginApp import LoginDialog 
from adminApp import VentanaAdmin
from usuarioApp import VentanaUsuario




if __name__ == "__main__":
    app = QApplication(sys.argv)

    login = LoginDialog()
    if login.exec():  # si el login fue aceptado
        data = login.user_data
        if data and data["valido"]:
            if data["rol"] == "admin":
                window= VentanaAdmin(data)
                window.show()
            else:
                 window= VentanaUsuario(data)
                 window.show()
            sys.exit(app.exec())

    sys.exit(0)