from PySide6.QtWidgets import QMainWindow
from admin import Ui_MainWindow  # importas la UI generada
from PySide6.QtCore import QSize  # para evitar problemas con QSize
from Funciones import *
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QTableWidgetItem
from datetime import datetime, date


class VentanaAdmin(QMainWindow, Ui_MainWindow):
    def __init__(self, resultado):
        super().__init__()
        # Inicializa la interfaz
        self.setupUi(self)
        self.id_usuario = resultado["id_usuario"]
        self.nombre=resultado["usuario"]
        
        self.label_usuario_2.setText(f"Hola: {self.nombre}")



        # Si quieres guardar el argumento que pasas
        self.resultado = resultado

        # Aquí puedes poner cualquier inicialización adicional
        self.setWindowTitle("Ventana Administrador")

       #Menu
        self.add_vehiculo_2.clicked.connect(self.DAgregar)        
        self.pagar_2.clicked.connect(self.DPagar)             
        self.pagar_ext_3.clicked.connect(self.DPagar_extravio)     
        self.add_pencion_2.clicked.connect(self.DPension)  
        self.borrar_ticket_2.clicked.connect(self.DBorrar)
        self.add_usuario_2.clicked.connect(self.DAgregarU)  
        self.mod_tarifa_2.clicked.connect(self.DCuota)
        self.reporte_2.clicked.connect(self.Dreporte)
        


        #Conexion combo box
        self.comboBox_12.currentIndexChanged.connect(self.on_combo_changed)
        self.on_combo_changed(self.comboBox_12.currentIndex())

        self.lineEdit_8.textChanged.connect(self.verificar_lineedits)
        self.lineEdit_9.textChanged.connect(self.verificar_lineedits)
        self.pushButton_7.setEnabled(False)

        self.lineEdit_10.textChanged.connect(self.verificar_lineedits)
        self.lineEdit_26.textChanged.connect(self.verificar_lineedits)
        self.pushButton_15.setEnabled(False)


        self.lineEdit_32.textChanged.connect(self.verificar_lineedits)
        self.pushButton_16.setEnabled(False)

        self.lineEdit_33.textChanged.connect(self.verificar_lineedits)
        self.plainTextEdit_3.textChanged.connect(self.verificar_lineedits)
        self.pushButton_17.setEnabled(False)






        self.lineEdit_34.textChanged.connect(self.verificar_lineedits)
        self.lineEdit_35.textChanged.connect(self.verificar_lineedits)
        self.lineEdit_36.textChanged.connect(self.verificar_lineedits)
        self.pushButton_18.setEnabled(False)


        self.comboBox_8.currentIndexChanged.connect(self.verificacionPencion)
   
        self.comboBox_9.currentIndexChanged.connect(self.verificacionPencion)
    
        self.comboBox_7.currentIndexChanged.connect(self.verificacionPencion)

        ##############actualizar tabla##########################################33
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.actualizartabla)  # conecta el timer a tu función
        self.timer.start(15000)  

        # Llamada inicial para llenar la tabla
        self.actualizartabla()



    #def clearALL(self):
      #  self.lineEdit.clear()
       # self.lineEdit_5.clear()
       # self.lineEdit_7.clear()
        #self.lineEdit_8.clear()
       # self.lineEdit_9.clear()
       # self.lineEdit_24.clear()
        #self.lineEdit_10.clear()
       # self.lineEdit_26.clear()
       # self.lineEdit_29.clear()
       # self.lineEdit_30.clear()
       # self.lineEdit_31.clear()
       # self.lineEdit_32.clear()
       # self.lineEdit_33.clear()
       # self.lineEdit_34.clear()
       # self.lineEdit_35.clear()
       # self.lineEdit_36.clear()
        #self.plainTextEdit_3.clear()
        
        
        
        

        
        
        
        
        
        
        
        
        
        

        


    
   
        






    
        




        #Button main conexion

        self.pushButton_5.clicked.connect(self.agregar_automovil)
        self.pushButton_6.clicked.connect(self.revisar_ticket)
        self.pushButton_19.clicked.connect(self.registrar_tarifa)
        self.pushButton_7.clicked.connect(self.cobrar_ticket)
        self.pushButton_8.clicked.connect(self.revisar_extravio)
        self.pushButton_16.clicked.connect(self.dar_alta)
        self.pushButton_18.clicked.connect(self.agregar_usuario_app)
        self.pushButton_15.clicked.connect(self.pagarExtra)
        self.pushButton_17.clicked.connect(self.borrarTicket)
        self.pushButton_20.clicked.connect(self.reporte)







             






 
########################Funciones de cambio app#########################3333
    def on_combo_changed(self, index):
        if index == 0:      # Opción 1
            self.doubleSpinBox_5.setEnabled(True)
            self.doubleSpinBox_6.setEnabled(True)
            self.doubleSpinBox_7.setValue(0)
            self.doubleSpinBox_8.setValue(0)
            self.doubleSpinBox_7.setEnabled(False)
            self.doubleSpinBox_8.setEnabled(False)
           
        elif index == 1:    # Opción 2
            self.doubleSpinBox_5.setValue(0)
            self.doubleSpinBox_6.setValue(0)
            self.doubleSpinBox_5.setEnabled(False)
            self.doubleSpinBox_6.setEnabled(False)
            self.doubleSpinBox_7.setEnabled(True)
            self.doubleSpinBox_8.setEnabled(True)
           
        else:               # Opción 3
            self.doubleSpinBox_5.setValue(0)
            self.doubleSpinBox_6.setValue(0)
            self.doubleSpinBox_7.setValue(0)
            self.doubleSpinBox_8.setValue(0)
            self.doubleSpinBox_5.setEnabled(False)
            self.doubleSpinBox_6.setEnabled(False)
            self.doubleSpinBox_7.setEnabled(False)
            self.doubleSpinBox_8.setEnabled(False)

    def DAgregar(self):
        self.stackedWidget.setCurrentIndex(0)
        #self.clearALL()
    def DPagar(self):
        self.stackedWidget.setCurrentIndex(1)
        #self.clearALL()
    def DPagar_extravio(self):
        self.stackedWidget.setCurrentIndex(2)
        #self.clearALL()
    def DPension(self):
        self.stackedWidget.setCurrentIndex(3)
        #self.clearALL()
    def DBorrar(self):
        self.stackedWidget.setCurrentIndex(4)
        #self.clearALL()
    def DAgregarU(self):
        self.stackedWidget.setCurrentIndex(5)
        #self.clearALL()
    def DCuota(self):
        self.stackedWidget.setCurrentIndex(6)
        #self.clearALL()
    def Dreporte(self):
        self.stackedWidget.setCurrentIndex(7)
        #self.clearALL()
    def verificar_lineedits(self):
        # Obtener el texto de ambos lineEdit
        texto1 = self.lineEdit_8.text().strip()
        texto2 = self.lineEdit_9.text().strip()

        texto3 = self.lineEdit_10.text().strip()
        texto4 = self.lineEdit_26.text().strip()

        texto5 =self.lineEdit_32.text().strip()

        texto6=self.lineEdit_34.text().strip()
        texto7=self.lineEdit_35.text().strip()
        texto8=self.lineEdit_36.text().strip()
    
        texto9= self.lineEdit_33.text().strip()
        texto10=self.plainTextEdit_3.toPlainText().strip()

        # Activar el botón solo si ambos tienen texto
        self.pushButton_7.setEnabled(bool(texto1) and bool(texto2))
        self.pushButton_15.setEnabled(bool(texto3) and bool(texto4))
        self.pushButton_16.setEnabled(bool(texto5))
        self.pushButton_18.setEnabled(bool(texto6) and bool(texto7) and bool(texto8))
        self.pushButton_17.setEnabled(bool(texto9) and bool(texto10))

    def verificacionPencion(self):
        tipoCliente=  self.comboBox_8.currentText().lower()
        tipoPension= self.comboBox_9.currentText().lower()
        tipoVehiculo= self.comboBox_7.currentText()
        if tipoVehiculo=="Automovil":
            tipoVehiculo="auto"
        else:
            tipoVehiculo="moto"


      
        respuesta=Precio_pension(tipoCliente,tipoVehiculo,tipoPension)
        self.lineEdit.setText(str(respuesta["Precio"]))





    ###Funciones app --> procedimientos 

    def agregar_automovil(self):
       placas = self.lineEdit_5.text().replace(" ", "").upper()
       tipo_vehiculo = self.comboBox.currentText()

       if  placas == "" :
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Warning)  # Icono de error
        msg.setWindowTitle("Advertencia")
        msg.setText("Se debe ingresar la placa  ")
        msg.setStandardButtons(QMessageBox.Ok)
        self.lineEdit_5.clear()
        msg.exec()

       elif tipo_vehiculo =="Automovil":
           resuktado= agregar_entrada(placas,"auto",self.id_usuario)
           if resuktado["Estado"] == "Error":
                msg = QMessageBox(self)
                msg.setIcon(QMessageBox.Critical)  # Icono de error
                msg.setWindowTitle("Error")
                msg.setText(resuktado["Mensaje"])
                msg.setStandardButtons(QMessageBox.Ok)
                self.lineEdit_5.clear()
                msg.exec()
           else:
                msg = QMessageBox(self)
                msg.setIcon(QMessageBox.Information)  # Icono de error
                msg.setWindowTitle("Exito")
                msg.setText(resuktado["Mensaje"])
                msg.setStandardButtons(QMessageBox.Ok)
                self.lineEdit_5.clear()
                imprimir_ticket(resuktado["codigo"])
                msg.exec()

       elif tipo_vehiculo=="Motocicleta":
        resuktado= agregar_entrada(placas,"moto",self.id_usuario)
        if resuktado["Estado"] == "Error":
                msg = QMessageBox(self)
                msg.setIcon(QMessageBox.Critical)  # Icono de error
                msg.setWindowTitle("Error")
                msg.setText(resuktado["Mensaje"])
                msg.setStandardButtons(QMessageBox.Ok)
                self.lineEdit_5.clear()
                msg.exec()
        else:
                msg = QMessageBox(self)
                msg.setIcon(QMessageBox.Information)  # Icono de error
                msg.setWindowTitle("Exito")
                msg.setText(resuktado["Mensaje"])
                msg.setStandardButtons(QMessageBox.Ok)
                self.lineEdit_5.clear()
                imprimir_ticket(resuktado["codigo"])
                msg.exec()


    def revisar_ticket(self):

        ticket = self.lineEdit_7.text().replace(" ", "").upper()
        
        if ticket == "" :
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Warning)  # Icono de error
            msg.setWindowTitle("Advertencia")
            msg.setText("Se debe ingresar el codigo de barras")
            msg.setStandardButtons(QMessageBox.Ok)
            self.lineEdit_7.clear()
            self.lineEdit_8.clear()
            self.lineEdit_9.clear()
            msg.exec()
        
        else:
           resultado= check_precio(ticket,self.id_usuario)
           print(resultado)
           if resultado["Estado"] == "Error":
                msg = QMessageBox(self)
                msg.setIcon(QMessageBox.Critical)  # Icono de error
                msg.setWindowTitle("Error")
                msg.setText(resultado["Mensaje"])
                msg.setStandardButtons(QMessageBox.Ok)
                self.lineEdit_7.clear()
                self.lineEdit_8.clear()
                self.lineEdit_9.clear()
                msg.exec()
           else:          
               self.lineEdit_9.setText(str(resultado["Precio"]))
               self.lineEdit_8.setText(str(resultado["codigo"]))



    def registrar_tarifa(self):
        tipo_vehiculo =self.comboBox_11.currentText()

        if tipo_vehiculo == 'Automovil':
            resultado= registrar_tarifa("auto",self.comboBox_12.currentText(),self.doubleSpinBox_5.value(),self.doubleSpinBox_6.value(),self.doubleSpinBox_7.value(),self.doubleSpinBox_8.value(),self.id_usuario)
            if resultado["Estado"] !="OK":

                msg = QMessageBox(self)
                msg.setIcon(QMessageBox.Critical)  # Icono de error
                msg.setWindowTitle("Error")
                msg.setText("No se pudo actualizar o insertar la tarifa")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec()
                self.doubleSpinBox_5.setValue(0)
                self.doubleSpinBox_6.setValue(0)
                self.doubleSpinBox_7.setValue(0)
                self.doubleSpinBox_8.setValue(0)
            else:
                msg = QMessageBox(self)
                msg.setIcon(QMessageBox.Information)  # Icono de error
                msg.setWindowTitle("Exito")
                msg.setText(resultado["Mensaje"])
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec()
                self.doubleSpinBox_5.setValue(0)
                self.doubleSpinBox_6.setValue(0)
                self.doubleSpinBox_7.setValue(0)
                self.doubleSpinBox_8.setValue(0)

        else:
            resultado= registrar_tarifa("moto",self.comboBox_12.currentText(),self.doubleSpinBox_5.value(),self.doubleSpinBox_6.value(),self.doubleSpinBox_7.value(),self.doubleSpinBox_8.value(),self.id_usuario)
            if resultado["Estado"] !="OK":

                msg = QMessageBox(self)
                msg.setIcon(QMessageBox.Critical)  # Icono de error
                msg.setWindowTitle("Error")
                msg.setText("No se pudo actualizar o insertar la tarifa")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec()
                self.doubleSpinBox_5.setValue(0)
                self.doubleSpinBox_6.setValue(0)
                self.doubleSpinBox_7.setValue(0)
                self.doubleSpinBox_8.setValue(0)
            else:
                msg = QMessageBox(self)
                msg.setIcon(QMessageBox.Information)  # Icono de error
                msg.setWindowTitle("Exito")
                msg.setText(resultado["Mensaje"])
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec()
                self.doubleSpinBox_5.setValue(0)
                self.doubleSpinBox_6.setValue(0)
                self.doubleSpinBox_7.setValue(0)
                self.doubleSpinBox_8.setValue(0)
        


    def cobrar_ticket(self):
        respuesta= pagar_precio(self.lineEdit_8.text(),self.id_usuario)
        if respuesta["Estado"]== "Error" or respuesta["Estado"]== "cerrado":
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Critical)  # Icono de error
            msg.setWindowTitle("Error")
            msg.setText(respuesta["Mensaje"])
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()
            self.lineEdit_7.clear()
            self.lineEdit_8.clear()
            self.lineEdit_9.clear()
        else:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Information)  # Icono de error
            msg.setWindowTitle("Error")
            msg.setText(respuesta["Mensaje"])
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()
            self.lineEdit_7.clear()
            self.lineEdit_8.clear()
            self.lineEdit_9.clear()
            

    def revisar_extravio(self):
        placa = self.lineEdit_24.text().replace(" ", "").upper()
        
        if placa == "" :
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Warning)  # Icono de error
            msg.setWindowTitle("Advertencia")
            msg.setText("Se debe ingresar el<numero de placa")
            msg.setStandardButtons(QMessageBox.Ok)
            self.lineEdit_10.clear()
            self.lineEdit_26.clear()
            msg.exec()
        
        else:
           resultado= check_precio_extravio(placa)
           print(resultado)
           print(resultado)
           if resultado["Estado"] == "Error":
                msg = QMessageBox(self)
                msg.setIcon(QMessageBox.Critical)  # Icono de error
                msg.setWindowTitle("Error")
                msg.setText(resultado["Mensaje"])
                msg.setStandardButtons(QMessageBox.Ok)
                self.lineEdit_10.clear()
                self.lineEdit_26.clear()
                msg.exec()
           else:          
               self.lineEdit_10.setText(str(resultado["Codigo"]))
               self.lineEdit_26.setText(str(resultado["Precio"]))

    def dar_alta(self):
        nombre=self.lineEdit_29.text().upper()
        telefono=self.lineEdit_30.text().replace(" ", "").upper()
        correo= self.lineEdit_31.text().replace(" ", "").upper()
        tipoCliente= self.comboBox_8.currentText()
        tipoPension=self.comboBox_9.currentText().lower()
        tipoVehiculo=self.comboBox_7.currentText()
        placa=self.lineEdit_32.text().replace(" ", "").upper()
        if tipoVehiculo == "Automovil":
            tipoVehiculo="auto"
        else:
            tipoVehiculo="moto"

        respuesta=agregar_cliente(nombre,telefono,correo,tipoCliente,tipoPension,placa,self.id_usuario,tipoVehiculo)

        if respuesta["Estado"]== "Error":
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Critical)  # Icono de error
            msg.setWindowTitle("Error")
            msg.setText(respuesta["Mensaje"])
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()
            self.lineEdit_29.clear()
            self.lineEdit_30.clear()
            self.lineEdit_31.clear()
            self.lineEdit_32.clear()
        else:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Information)  # Icono de error
            msg.setWindowTitle("Exito")
            msg.setText(respuesta["Mensaje"])
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()
            self.lineEdit_29.clear()
            self.lineEdit_30.clear()
            self.lineEdit_31.clear()
            self.lineEdit_32.clear()
            self.lineEdit.clear()
            

    def agregar_usuario_app(self):
        Usuario=self.lineEdit_34.text().lower()
        contrasena=self.lineEdit_35.text()
        nombre= self.lineEdit_36.text().upper()
        tipo=self.comboBox_10.currentText()
        if tipo == "Administrador":
            resultado= add_usuario(Usuario,contrasena,nombre,self.id_usuario,"admin")
            print(resultado)
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Warning)  # Icono de error
            msg.setWindowTitle("Advertencia")
            msg.setText(resultado["Mensaje"])
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()
            self.lineEdit_34.clear()
            self.lineEdit_35.clear()
            self.lineEdit_36.clear()

        else:
            resultado= add_usuario(Usuario,contrasena,nombre,self.id_usuario,"empleado")
            print(resultado)
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Warning)  # Icono de error
            msg.setWindowTitle("Advertencia")
            msg.setText(resultado["Mensaje"])
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()
            self.lineEdit_34.clear()
            self.lineEdit_35.clear()
            self.lineEdit_36.clear()


    def pagarExtra(self):
        ticket=self.lineEdit_10.text()
        respuesta=pagar_precio_Extravio(ticket,self.id_usuario)
        if respuesta["Estado"]== "Error" or respuesta["Estado"]== "cerrado":
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Critical)  # Icono de error
            msg.setWindowTitle("Error")
            msg.setText(respuesta["Mensaje"])
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()
            self.lineEdit_7.clear()
            self.lineEdit_8.clear()
            self.lineEdit_9.clear()
        else:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Information)  # Icono de error
            msg.setWindowTitle("Error")
            msg.setText(respuesta["Mensaje"])
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()
            self.lineEdit_7.clear()
            self.lineEdit_8.clear()
            self.lineEdit_9.clear()
            

    def borrarTicket(self):
        codigo= self.lineEdit_33.text()
        motivo=self.plainTextEdit_3.toPlainText()
        print(codigo,motivo)
        resultado= eliminar_Ticket(codigo,motivo,self.id_usuario)
        if resultado["Estado"]== "Error":
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Critical)  # Icono de error
            msg.setWindowTitle("Error")
            msg.setText(resultado["Mensaje"])
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()
            self.lineEdit_33.clear()
            self.plainTextEdit_3.clear()
        else:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Information)  # Icono de error
            msg.setWindowTitle("Error")
            msg.setText(resultado["Mensaje"])
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()
            self.lineEdit_33.clear()
            self.plainTextEdit_3.clear()
            self.lineEdit.clear()




    def reporte(self):
        fecha_inicio=self.calendarWidget_5.selectedDate().toString("yyyy-MM-dd")
        fecha_final=self.calendarWidget_6.selectedDate().toString("yyyy-MM-dd")
        respuesta= dar_reporte(fecha_inicio,fecha_final,self.id_usuario,)
        if respuesta == []:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Information)  # Icono de error
            msg.setWindowTitle("Error")
            msg.setText("No se encontro ningun registro de esas fechas")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()
        else:
            nombrereporte="Reporte del "+fecha_inicio+" al " +fecha_final+".xlsx"
            print(nombrereporte)
            reporteExcel(respuesta,nombrereporte,"cuicavision@gmail.com")
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Information)  # Icono de error
            msg.setWindowTitle("Exito")
            msg.setText("Se realizo el reporte con exito")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()


    def actualizartabla(self):
        rows = autosActivos()
        print("Datos recibidos:", rows)

        self.tableWidget_2.setRowCount(0)  # limpiar la tabla
        self.tableWidget_2.setColumnCount(4)  # aseguramos 4 columnas
        self.tableWidget_2.setHorizontalHeaderLabels(["ID Ticket", "Código", "Placas", "Hora Entrada"])

        for i, row in enumerate(rows):
            print(f"Fila {i}: {row}")  # debug para ver cada fila
            self.tableWidget_2.insertRow(i)
            for j, value in enumerate(row):
                if isinstance(value, (datetime, date)):
                    value = value.strftime("%Y-%m-%d %H:%M:%S")
                print(f"  Columna {j}: {value}")  # debug para ver cada valor
                self.tableWidget_2.setItem(i, j, QTableWidgetItem(str(value)))

    # Ajusta automáticamente el ancho de columnas
        
        


