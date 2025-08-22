# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)
import iconos_rc
import iconos_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(337, 198)
        Dialog.setMinimumSize(QSize(337, 198))
        Dialog.setMaximumSize(QSize(337, 198))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        Dialog.setFont(font)
        Dialog.setStyleSheet(u"QWidget {\n"
"    background-color: #f4f6f9;\n"
"    font-family: 'Segoe UI', sans-serif;\n"
"}")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 80, 65, 18))
        self.label.setMaximumSize(QSize(65, 18))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"QLabel {\n"
"    color: #2c3e50;\n"
"    font-size: 14px;\n"
"}")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 109, 101, 31))
        self.label_2.setMinimumSize(QSize(101, 20))
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"QLabel {\n"
"    color: #2c3e50;\n"
"    font-size: 14px;\n"
"}")
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(60, 70, 24, 24))
        self.label_3.setMinimumSize(QSize(24, 24))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(9)
        self.label_3.setFont(font2)
        self.label_3.setPixmap(QPixmap(u":/prefijoNuevo/user.svg"))
        self.label_3.setScaledContents(True)
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 110, 21, 21))
        self.label_4.setMinimumSize(QSize(21, 21))
        self.label_4.setPixmap(QPixmap(u":/prefijoNuevo/lock.svg"))
        self.label_4.setScaledContents(True)
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(160, 70, 141, 31))
        self.lineEdit.setMinimumSize(QSize(141, 31))
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #dfe6e9;\n"
"    border-radius: 8px;\n"
"    padding: 6px 10px;\n"
"    font-size: 14px;\n"
"    background: #ffffff;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid #1a73e8;\n"
"    background: #f9fcff;\n"
"}")
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(120, 150, 111, 41))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #1a73e8;\n"
"    color: white;\n"
"    border-radius: 8px;\n"
"    padding: 8px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #155ab6;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #0d3c91;\n"
"}")
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 20, 291, 41))
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"QLabel {\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    color: #1a73e8;\n"
"    margin-bottom: 10px;\n"
"}")
        self.lineEdit_2 = QLineEdit(Dialog)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(160, 110, 141, 31))
        self.lineEdit_2.setMinimumSize(QSize(141, 31))
        self.lineEdit_2.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #dfe6e9;\n"
"    border-radius: 8px;\n"
"    padding: 6px 10px;\n"
"    font-size: 14px;\n"
"    background: #ffffff;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid #1a73e8;\n"
"    background: #f9fcff;\n"
"}")
        self.lineEdit_2.setEchoMode(QLineEdit.EchoMode.Password)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Login Estacionamiento ", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Usuario:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Contrase\u00f1a:", None))
        self.label_3.setText("")
        self.label_4.setText("")
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Entrar", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Introduce Usuario y contrase\u00f1a", None))
    # retranslateUi

