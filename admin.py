# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'admin2.ui'
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QComboBox, QDoubleSpinBox,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import iconos_rc
import iconos_rc
import iconos_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 854)
        MainWindow.setMinimumSize(QSize(1200, 846))
        MainWindow.setMaximumSize(QSize(1200, 16777215))
        font = QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: #f0f8ff;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.iconoText = QWidget(self.centralwidget)
        self.iconoText.setObjectName(u"iconoText")
        self.iconoText.setMaximumSize(QSize(191, 849))
        self.iconoText.setStyleSheet(u"QPushButtons{\n"
" height:30px;\n"
" border:none;\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.iconoText)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 20, -1, 15)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 6)
        self.label_2 = QLabel(self.iconoText)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(31, 31))
        self.label_2.setPixmap(QPixmap(u":/prefijoNuevo/images.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.iconoText)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setBold(True)
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"QLabel {\n"
"    font-size: 15px;                  /* grande y llamativo */\n"
"    font-weight: bold;                 /* negrita */\n"
"    color: #2980b9;                    /* azul principal */\n"
"    letter-spacing: 1px;               /* espacio entre letras */\n"
"    text-shadow: 1px 1px 2px rgba(0,0,0,0.2); /* sombra sutil */\n"
"    font-family: \"Segoe UI\", \"Arial\", sans-serif; /* moderna y legible */\n"
"}")

        self.horizontalLayout.addWidget(self.label_3)


        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(13)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 20, -1, -1)
        self.add_vehiculo_2 = QPushButton(self.iconoText)
        self.add_vehiculo_2.setObjectName(u"add_vehiculo_2")
        self.add_vehiculo_2.setStyleSheet(u"QPushButton {\n"
"    background-color:#d7e9ff;        /* azul muy suave de base */\n"
"    color: #2c3e50;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    padding: 10px 16px;\n"
"    font-size: 14px;\n"
"    text-align: left;               /* alineado a la izquierda */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #d7e9ff;      /* azul un poco m\u00e1s intenso al pasar el mouse */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #a9d1ff;      /* azul m\u00e1s oscuro al hacer clic */\n"
"    color: #0b3d91;                 /* texto m\u00e1s fuerte */\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* bot\u00f3n \"activo\" \u2192 lo puedes aplicar con setProperty(\"class\", \"active\") */\n"
"QPushButton[active=\"true\"] {\n"
"    background-color: #3498db;      /* azul fuerte */\n"
"    color: white;\n"
"    font-weight: bold;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/prefijoNuevo/add-car-icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.add_vehiculo_2.setIcon(icon)
        self.add_vehiculo_2.setIconSize(QSize(200, 20))
        self.add_vehiculo_2.setCheckable(True)
        self.add_vehiculo_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.add_vehiculo_2)

        self.pagar_2 = QPushButton(self.iconoText)
        self.pagar_2.setObjectName(u"pagar_2")
        self.pagar_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #d7e9ff;        /* azul muy suave de base */\n"
"    color: #2c3e50;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    padding: 10px 16px;\n"
"    font-size: 14px;\n"
"    text-align: left;               /* alineado a la izquierda */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #d7e9ff;      /* azul un poco m\u00e1s intenso al pasar el mouse */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #a9d1ff;      /* azul m\u00e1s oscuro al hacer clic */\n"
"    color: #0b3d91;                 /* texto m\u00e1s fuerte */\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* bot\u00f3n \"activo\" \u2192 lo puedes aplicar con setProperty(\"class\", \"active\") */\n"
"QPushButton[active=\"true\"] {\n"
"    background-color: #3498db;      /* azul fuerte */\n"
"    color: white;\n"
"    font-weight: bold;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/prefijoNuevo/dollar-sign.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pagar_2.setIcon(icon1)
        self.pagar_2.setIconSize(QSize(100, 20))
        self.pagar_2.setCheckable(True)
        self.pagar_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.pagar_2)

        self.pagar_ext_3 = QPushButton(self.iconoText)
        self.pagar_ext_3.setObjectName(u"pagar_ext_3")
        self.pagar_ext_3.setStyleSheet(u"QPushButton {\n"
"    background-color: #d7e9ff;        /* azul muy suave de base */\n"
"    color: #2c3e50;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    padding: 10px 16px;\n"
"    font-size: 14px;\n"
"    text-align: left;               /* alineado a la izquierda */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #d7e9ff;      /* azul un poco m\u00e1s intenso al pasar el mouse */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #a9d1ff;      /* azul m\u00e1s oscuro al hacer clic */\n"
"    color: #0b3d91;                 /* texto m\u00e1s fuerte */\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* bot\u00f3n \"activo\" \u2192 lo puedes aplicar con setProperty(\"class\", \"active\") */\n"
"QPushButton[active=\"true\"] {\n"
"    background-color: #3498db;      /* azul fuerte */\n"
"    color: white;\n"
"    font-weight: bold;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/prefijoNuevo/remove-ticket-icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pagar_ext_3.setIcon(icon2)
        self.pagar_ext_3.setIconSize(QSize(100, 20))
        self.pagar_ext_3.setCheckable(True)
        self.pagar_ext_3.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.pagar_ext_3)

        self.add_pencion_2 = QPushButton(self.iconoText)
        self.add_pencion_2.setObjectName(u"add_pencion_2")
        self.add_pencion_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #d7e9ff;        /* azul muy suave de base */\n"
"    color: #2c3e50;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    padding: 10px 16px;\n"
"    font-size: 14px;\n"
"    text-align: left;               /* alineado a la izquierda */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #d7e9ff;      /* azul un poco m\u00e1s intenso al pasar el mouse */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #a9d1ff;      /* azul m\u00e1s oscuro al hacer clic */\n"
"    color: #0b3d91;                 /* texto m\u00e1s fuerte */\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* bot\u00f3n \"activo\" \u2192 lo puedes aplicar con setProperty(\"class\", \"active\") */\n"
"QPushButton[active=\"true\"] {\n"
"    background-color: #3498db;      /* azul fuerte */\n"
"    color: white;\n"
"    font-weight: bold;\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/prefijoNuevo/add-boy-user-icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.add_pencion_2.setIcon(icon3)
        self.add_pencion_2.setIconSize(QSize(100, 20))
        self.add_pencion_2.setCheckable(True)
        self.add_pencion_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.add_pencion_2)

        self.borrar_ticket_2 = QPushButton(self.iconoText)
        self.borrar_ticket_2.setObjectName(u"borrar_ticket_2")
        self.borrar_ticket_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #d7e9ff;        /* azul muy suave de base */\n"
"    color: #2c3e50;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    padding: 10px 16px;\n"
"    font-size: 14px;\n"
"    text-align: left;               /* alineado a la izquierda */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #d7e9ff;      /* azul un poco m\u00e1s intenso al pasar el mouse */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #a9d1ff;      /* azul m\u00e1s oscuro al hacer clic */\n"
"    color: #0b3d91;                 /* texto m\u00e1s fuerte */\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* bot\u00f3n \"activo\" \u2192 lo puedes aplicar con setProperty(\"class\", \"active\") */\n"
"QPushButton[active=\"true\"] {\n"
"    background-color: #3498db;      /* azul fuerte */\n"
"    color: white;\n"
"    font-weight: bold;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/prefijoNuevo/trash-2.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.borrar_ticket_2.setIcon(icon4)
        self.borrar_ticket_2.setIconSize(QSize(100, 20))
        self.borrar_ticket_2.setCheckable(True)
        self.borrar_ticket_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.borrar_ticket_2)


        self.verticalLayout_5.addLayout(self.verticalLayout_2)

        self.verticalSpacer_4 = QSpacerItem(20, 164, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_4)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, -1, 18)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, -1, -1, 10)
        self.label = QLabel(self.iconoText)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(25, 25))
        self.label.setPixmap(QPixmap(u":/prefijoNuevo/man-working-on-laptop-icon.svg"))
        self.label.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.label)

        self.label_5 = QLabel(self.iconoText)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"QLabel {\n"
"    font-size: 15px;                  /* grande y llamativo */\n"
"    font-weight: bold;                 /* negrita */\n"
"    color: #2980b9;                    /* azul principal */\n"
"    letter-spacing: 1px;               /* espacio entre letras */\n"
"    text-shadow: 1px 1px 2px rgba(0,0,0,0.2); /* sombra sutil */\n"
"    font-family: \"Segoe UI\", \"Arial\", sans-serif; /* moderna y legible */\n"
"}")

        self.horizontalLayout_6.addWidget(self.label_5)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.add_usuario_2 = QPushButton(self.iconoText)
        self.add_usuario_2.setObjectName(u"add_usuario_2")
        self.add_usuario_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #d7e9ff;        /* azul muy suave de base */\n"
"    color: #2c3e50;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    padding: 10px 16px;\n"
"    font-size: 14px;\n"
"    text-align: left;               /* alineado a la izquierda */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #d7e9ff;      /* azul un poco m\u00e1s intenso al pasar el mouse */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #a9d1ff;      /* azul m\u00e1s oscuro al hacer clic */\n"
"    color: #0b3d91;                 /* texto m\u00e1s fuerte */\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* bot\u00f3n \"activo\" \u2192 lo puedes aplicar con setProperty(\"class\", \"active\") */\n"
"QPushButton[active=\"true\"] {\n"
"    background-color: #3498db;      /* azul fuerte */\n"
"    color: white;\n"
"    font-weight: bold;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/prefijoNuevo/create-group-icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.add_usuario_2.setIcon(icon5)
        self.add_usuario_2.setIconSize(QSize(100, 20))
        self.add_usuario_2.setCheckable(True)
        self.add_usuario_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.add_usuario_2)

        self.mod_tarifa_2 = QPushButton(self.iconoText)
        self.mod_tarifa_2.setObjectName(u"mod_tarifa_2")
        self.mod_tarifa_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #d7e9ff;        /* azul muy suave de base */\n"
"    color: #2c3e50;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    padding: 10px 16px;\n"
"    font-size: 14px;\n"
"    text-align: left;               /* alineado a la izquierda */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #d7e9ff;      /* azul un poco m\u00e1s intenso al pasar el mouse */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #a9d1ff;      /* azul m\u00e1s oscuro al hacer clic */\n"
"    color: #0b3d91;                 /* texto m\u00e1s fuerte */\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* bot\u00f3n \"activo\" \u2192 lo puedes aplicar con setProperty(\"class\", \"active\") */\n"
"QPushButton[active=\"true\"] {\n"
"    background-color: #3498db;      /* azul fuerte */\n"
"    color: white;\n"
"    font-weight: bold;\n"
"}\n"
"")
        icon6 = QIcon()
        icon6.addFile(u":/prefijoNuevo/money-icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.mod_tarifa_2.setIcon(icon6)
        self.mod_tarifa_2.setIconSize(QSize(100, 20))
        self.mod_tarifa_2.setCheckable(True)
        self.mod_tarifa_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.mod_tarifa_2)

        self.reporte_2 = QPushButton(self.iconoText)
        self.reporte_2.setObjectName(u"reporte_2")
        self.reporte_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #d7e9ff;        /* azul muy suave de base */\n"
"    color: #2c3e50;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    padding: 10px 16px;\n"
"    font-size: 14px;\n"
"    text-align: left;               /* alineado a la izquierda */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #d7e9ff;      /* azul un poco m\u00e1s intenso al pasar el mouse */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #a9d1ff;      /* azul m\u00e1s oscuro al hacer clic */\n"
"    color: #0b3d91;                 /* texto m\u00e1s fuerte */\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* bot\u00f3n \"activo\" \u2192 lo puedes aplicar con setProperty(\"class\", \"active\") */\n"
"QPushButton[active=\"true\"] {\n"
"    background-color: #3498db;      /* azul fuerte */\n"
"    color: white;\n"
"    font-weight: bold;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/prefijoNuevo/column-chart-line-icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.reporte_2.setIcon(icon7)
        self.reporte_2.setIconSize(QSize(100, 20))
        self.reporte_2.setCheckable(True)
        self.reporte_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.reporte_2)


        self.verticalLayout_5.addLayout(self.verticalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 338, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.exit_2 = QPushButton(self.iconoText)
        self.exit_2.setObjectName(u"exit_2")
        self.exit_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #d7e9ff;        /* azul muy suave de base */\n"
"    color: #2c3e50;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    padding: 10px 16px;\n"
"    font-size: 14px;\n"
"    text-align: left;               /* alineado a la izquierda */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #d7e9ff;      /* azul un poco m\u00e1s intenso al pasar el mouse */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #ED2828;      /* azul m\u00e1s oscuro al hacer clic */\n"
"    color: #0b3d91;                 /* texto m\u00e1s fuerte */\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* bot\u00f3n \"activo\" \u2192 lo puedes aplicar con setProperty(\"class\", \"active\") */\n"
"QPushButton[active=\"true\"] {\n"
"    background-color: #3498db;      /* azul fuerte */\n"
"    color: white;\n"
"    font-weight: bold;\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/prefijoNuevo/log-out.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.exit_2.setIcon(icon8)
        self.exit_2.setIconSize(QSize(100, 20))
        self.exit_2.setCheckable(True)
        self.exit_2.setAutoExclusive(True)

        self.horizontalLayout_5.addWidget(self.exit_2)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)


        self.horizontalLayout_2.addWidget(self.iconoText)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.widget_4 = QWidget(self.centralwidget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(831, 0))
        self.widget_4.setStyleSheet(u"QWidget {\n"
"    background-color: #d7e9ff;       /* azul muy suave, armoniza con botones */\n"
"    color: #0b3d91;                  /* texto azul oscuro para contraste */\n"
"    font-size: 24px;                  /* tama\u00f1o grande para destacar */\n"
"    font-weight: bold;                /* negrita */\n"
"    padding: 12px 20px;               /* espacio interno */\n"
"    border-bottom: 2px solid #a9d1ff;/* separador sutil */\n"
"    border-top-left-radius: 8px;      /* bordes redondeados arriba */\n"
"    border-top-right-radius: 8px;\n"
"    text-align: left;                 /* texto alineado a la izquierda */\n"
"}")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(10, -1, -1, -1)
        self.label_usuario_2 = QLabel(self.widget_4)
        self.label_usuario_2.setObjectName(u"label_usuario_2")
        font2 = QFont()
        font2.setBold(True)
        self.label_usuario_2.setFont(font2)

        self.verticalLayout_9.addWidget(self.label_usuario_2)

        self.label_rol_2 = QLabel(self.widget_4)
        self.label_rol_2.setObjectName(u"label_rol_2")
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(14)
        font3.setBold(False)
        font3.setItalic(False)
        self.label_rol_2.setFont(font3)
        self.label_rol_2.setStyleSheet(u"color: rgb(156, 156, 156);\n"
"font: 14pt \"Segoe UI\";")

        self.verticalLayout_9.addWidget(self.label_rol_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_9)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_3)

        self.horizontalSpacer_8 = QSpacerItem(696, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_8)


        self.verticalLayout_8.addWidget(self.widget_4)

        self.main = QWidget(self.centralwidget)
        self.main.setObjectName(u"main")
        self.main.setMinimumSize(QSize(841, 741))
        self.main.setMaximumSize(QSize(1200, 741))
        font4 = QFont()
        font4.setPointSize(2)
        self.main.setFont(font4)
        self.main.setStyleSheet(u"")
        self.gridLayout_2 = QGridLayout(self.main)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.stackedWidget = QStackedWidget(self.main)
        self.stackedWidget.setObjectName(u"stackedWidget")
        font5 = QFont()
        font5.setPointSize(16)
        self.stackedWidget.setFont(font5)
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.tableWidget_2 = QTableWidget(self.page_9)
        if (self.tableWidget_2.columnCount() < 4):
            self.tableWidget_2.setColumnCount(4)
        font6 = QFont()
        font6.setPointSize(16)
        font6.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font6);
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font6);
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font6);
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font6);
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setGeometry(QRect(0, 90, 961, 591))
        self.tableWidget_2.setStyleSheet(u"/* ===== QTableWidget (base) ===== */\n"
"QTableWidget {\n"
"    background: #ffffff;\n"
"    color: #2c3e50;\n"
"    gridline-color: #e6e6e6;\n"
"    selection-background-color: #e9f3ff;  /* fallback si el estilo no toma el de item */\n"
"    selection-color: #0b3d91;\n"
"    alternate-background-color: #fafafa;  /* activar alternatingRowColors=true */\n"
"    border: 1px solid #e1e1e1;\n"
"    border-radius: 8px;\n"
"    outline: 0; /* quita el enfoque punteado */\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"/* ===== Filas / celdas ===== */\n"
"QAbstractItemView::item {\n"
"    padding: 8px 12px;          /* \u201caltura\u201d visual de fila */\n"
"    border: 0px;                /* las l\u00edneas las pone gridline-color */\n"
"}\n"
"QAbstractItemView::item:hover {\n"
"    background: #f5faff;\n"
"}\n"
"QAbstractItemView::item:selected {\n"
"    background: #d7e9ff;\n"
"    color: #0b3d91;\n"
"}\n"
"\n"
"/* ===== Encabezados ===== */\n"
"QHeaderView::section {\n"
"    background: #f6f7f9;\n"
"    color: #4a4a4a;"
                        "\n"
"    padding: 10px 12px;\n"
"    border: 0px;\n"
"    border-right: 1px solid #e6e6e6;\n"
"    font-weight: 600;\n"
"}\n"
"QHeaderView::section:last {\n"
"    border-right: 0;\n"
"}\n"
"QHeaderView::section:pressed {\n"
"    background: #edf1f7;\n"
"}\n"
"QHeaderView::down-arrow, QHeaderView::up-arrow {\n"
"    width: 10px; height: 10px;  /* tama\u00f1o de icono de sort */\n"
"}\n"
"QScrollBar:vertical {\n"
"    background: transparent;\n"
"    width: 10px;\n"
"    margin: 2px 2px 2px 2px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: #dcdcdc;\n"
"    min-height: 24px;\n"
"    border-radius: 5px;\n"
"}\n"
"QScrollBar::handle:vertical:hover { background: #cfcfcf; }\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical { height: 0; }\n"
"\n"
"QScrollBar:horizontal {\n"
"    background: transparent;\n"
"    height: 10px;\n"
"    margin: 2px 2px 2px 2px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: #dcdcdc;\n"
"    min-width: 24px;\n"
"    border-radius: 5px;\n"
"}\n"
""
                        "QScrollBar::handle:horizontal:hover { background: #cfcfcf; }")
        self.tableWidget_2.horizontalHeader().setVisible(True)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.horizontalHeader().setMinimumSectionSize(67)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(239)
        self.tableWidget_2.horizontalHeader().setHighlightSections(False)
        self.tableWidget_2.verticalHeader().setMinimumSectionSize(52)
        self.tableWidget_2.verticalHeader().setDefaultSectionSize(52)
        self.pushButton_5 = QPushButton(self.page_9)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(640, 10, 161, 71))
        self.pushButton_5.setFont(font2)
        self.pushButton_5.setStyleSheet(u"QPushButton:disabled {\n"
"    background-color: #bdc3c7;   /* gris apagado */\n"
"    color: #7f8c8d;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    padding: 10px 20px;\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:enabled {\n"
"    background-color: #2980b9;   /* azul arm\u00f3nico */\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    padding: 10px 20px;\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:enabled:hover {\n"
"    background-color: #3498db;   /* azul m\u00e1s claro */\n"
"}\n"
"\n"
"QPushButton:enabled:pressed {\n"
"    background-color: #2D9623;   /* azul m\u00e1s oscuro */\n"
"}")
        self.lineEdit_5 = QLineEdit(self.page_9)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(40, 20, 271, 61))
        font7 = QFont()
        self.lineEdit_5.setFont(font7)
        self.lineEdit_5.setStyleSheet(u"QLineEdit {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #e0e0e0;\n"
"    border-radius: 8px;\n"
"    padding: 6px 10px;\n"
"    font-size: 14px;\n"
"    color: #2c3e50;\n"
"    selection-background-color: #d7e9ff; /* color del texto seleccionado */\n"
"    selection-color: #0b3d91;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #3498db;  /* azul suave al enfocar */\n"
"    background-color: #f9fcff;\n"
"    outline: none;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: #f0f0f0;\n"
"    color: #a0a0a0;\n"
"    border: 2px solid #d0d0d0;\n"
"}")
        self.comboBox = QComboBox(self.page_9)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(340, 20, 191, 61))
        self.comboBox.setStyleSheet(u"QComboBox {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #e0e0e0;\n"
"    border-radius: 8px;\n"
"    padding: 6px 10px;\n"
"    font-size: 14px;\n"
"    color: #2c3e50;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 2px solid #b0c4de;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 2px solid #3498db;\n"
"    background-color: #f9fcff;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 24px;\n"
"    border-left: 1px solid #e0e0e0;\n"
"    border-top-right-radius: 6px;\n"
"    border-bottom-right-radius: 6px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* === ESTILO DEL DESPLEGABLE === */\n"
"QComboBox QAbstractItemView {\n"
"    background: #ffffff;\n"
"    border: 1px solid #e0e0e0;\n"
"    border-radius: 8px;\n"
"    padding: 4px;\n"
"    outline: 0;\n"
"    selection-background-color: #d7e9ff;\n"
"    selection-color: #0b3d91;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"    padding: 6px 10px;\n"
""
                        "}\n"
"\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background: #f5faff;\n"
"}")
        self.stackedWidget.addWidget(self.page_9)
        self.page_10 = QWidget()
        self.page_10.setObjectName(u"page_10")
        self.pushButton_6 = QPushButton(self.page_10)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(550, 100, 161, 41))
        self.pushButton_6.setFont(font2)
        self.pushButton_6.setStyleSheet(u"QPushButton:disabled {\n"
"    background-color: #bdc3c7;   /* gris apagado */\n"
"    color: #7f8c8d;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    padding: 10px 20px;\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:enabled {\n"
"    background-color: #2980b9;   /* azul arm\u00f3nico */\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    padding: 10px 20px;\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:enabled:hover {\n"
"    background-color: #3498db;   /* azul m\u00e1s claro */\n"
"}\n"
"\n"
"QPushButton:enabled:pressed {\n"
"    background-color: #1E1E63;   /* azul m\u00e1s oscuro */\n"
"}")
        self.lineEdit_7 = QLineEdit(self.page_10)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(270, 100, 261, 41))
        self.lineEdit_7.setFont(font7)
        self.lineEdit_7.setStyleSheet(u"QLineEdit {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #e0e0e0;\n"
"    border-radius: 8px;\n"
"    padding: 6px 10px;\n"
"    font-size: 14px;\n"
"    color: #2c3e50;\n"
"    selection-background-color: #d7e9ff; /* color del texto seleccionado */\n"
"    selection-color: #0b3d91;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #3498db;  /* azul suave al enfocar */\n"
"    background-color: #f9fcff;\n"
"    outline: none;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: #f0f0f0;\n"
"    color: #a0a0a0;\n"
"    border: 2px solid #d0d0d0;\n"
"}")
        self.label_7 = QLabel(self.page_10)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(270, 230, 71, 41))
        self.label_7.setFont(font2)
        self.label_7.setStyleSheet(u"QLabel {\n"
"    color: #2c3e50;        /* texto oscuro y elegante */\n"
"    font-size: 20px;        /* tama\u00f1o legible */\n"
"    font-weight: bold;       /* negrita para resaltar */\n"
"    padding: 2px 0;          /* un poco de espacio arriba y abajo */\n"
"}")
        self.label_8 = QLabel(self.page_10)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(270, 330, 71, 21))
        self.label_8.setFont(font2)
        self.label_8.setStyleSheet(u"QLabel {\n"
"    color: #2c3e50;        /* texto oscuro y elegante */\n"
"    font-size: 20px;        /* tama\u00f1o legible */\n"
"    font-weight: bold;       /* negrita para resaltar */\n"
"    padding: 2px 0;          /* un poco de espacio arriba y abajo */\n"
"}")
        self.lineEdit_8 = QLineEdit(self.page_10)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setGeometry(QRect(360, 230, 301, 51))
        self.lineEdit_8.setFont(font7)
        self.lineEdit_8.setStyleSheet(u"QLineEdit {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #e0e0e0;\n"
"    border-radius: 8px;\n"
"    padding: 6px 10px;\n"
"    font-size: 14px;\n"
"    color: #2c3e50;\n"
"    selection-background-color: #d7e9ff; /* color del texto seleccionado */\n"
"    selection-color: #0b3d91;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #3498db;  /* azul suave al enfocar */\n"
"    background-color: #f9fcff;\n"
"    outline: none;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: #f0f0f0;\n"
"    color: #a0a0a0;\n"
"    border: 2px solid #d0d0d0;\n"
"}")
        self.lineEdit_8.setReadOnly(True)
        self.lineEdit_9 = QLineEdit(self.page_10)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setGeometry(QRect(370, 310, 181, 51))
        self.lineEdit_9.setFont(font7)
        self.lineEdit_9.setStyleSheet(u"QLineEdit {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #e0e0e0;\n"
"    border-radius: 8px;\n"
"    padding: 6px 10px;\n"
"    font-size: 14px;\n"
"    color: #2c3e50;\n"
"    selection-background-color: #d7e9ff; /* color del texto seleccionado */\n"
"    selection-color: #0b3d91;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #3498db;  /* azul suave al enfocar */\n"
"    background-color: #f9fcff;\n"
"    outline: none;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: #f0f0f0;\n"
"    color: #a0a0a0;\n"
"    border: 2px solid #d0d0d0;\n"
"}")
        self.lineEdit_9.setReadOnly(True)
        self.pushButton_7 = QPushButton(self.page_10)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(400, 390, 181, 81))
        self.pushButton_7.setFont(font2)
        self.pushButton_7.setStyleSheet(u"QPushButton:disabled {\n"
"    background-color: #bdc3c7;   /* gris apagado */\n"
"    color: #7f8c8d;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    padding: 10px 20px;\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:enabled {\n"
"    background-color: #2980b9;   /* azul arm\u00f3nico */\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    padding: 10px 20px;\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:enabled:hover {\n"
"    background-color: #3498db;   /* azul m\u00e1s claro */\n"
"}\n"
"\n"
"QPushButton:enabled:pressed {\n"
"    background-color: #2D9623;   /* azul m\u00e1s oscuro */\n"
"}")
        self.label_15 = QLabel(self.page_10)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(10, 10, 961, 91))
        self.label_15.setFont(font2)
        self.label_15.setStyleSheet(u"QLabel {\n"
"    font-size: 26px;           /* m\u00e1s grande */\n"
"    font-weight: bold;\n"
"    color: #3498db;            /* azul destacado */\n"
"    padding: 10px 14px;\n"
"    border-left: 5px solid #3498db;  /* l\u00ednea lateral m\u00e1s gruesa */\n"
"    background-color: #f0f8ff;       /* fondo sutil opcional */\n"
"    margin-bottom: 12px;\n"
"}")
        self.stackedWidget.addWidget(self.page_10)
        self.page_11 = QWidget()
        self.page_11.setObjectName(u"page_11")
        self.lineEdit_10 = QLineEdit(self.page_11)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setGeometry(QRect(360, 200, 241, 41))
        self.lineEdit_10.setFont(font7)
        self.lineEdit_10.setStyleSheet(u"QLineEdit {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #e0e0e0;\n"
"    border-radius: 8px;\n"
"    padding: 6px 10px;\n"
"    font-size: 14px;\n"
"    color: #2c3e50;\n"
"    selection-background-color: #d7e9ff; /* color del texto seleccionado */\n"
"    selection-color: #0b3d91;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #3498db;  /* azul suave al enfocar */\n"
"    background-color: #f9fcff;\n"
"    outline: none;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: #f0f0f0;\n"
"    color: #a0a0a0;\n"
"    border: 2px solid #d0d0d0;\n"
"}")
        self.lineEdit_10.setReadOnly(True)
        self.label_32 = QLabel(self.page_11)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(60, 270, 281, 41))
        self.label_32.setFont(font2)
        self.label_32.setStyleSheet(u"QLabel {\n"
"    color: #2c3e50;        /* texto oscuro y elegante */\n"
"    font-size: 20px;        /* tama\u00f1o legible */\n"
"    font-weight: bold;       /* negrita para resaltar */\n"
"    padding: 2px 0;          /* un poco de espacio arriba y abajo */\n"
"}")
        self.label_48 = QLabel(self.page_11)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setGeometry(QRect(260, 210, 81, 31))
        self.label_48.setFont(font2)
        self.label_48.setStyleSheet(u"QLabel {\n"
"    color: #2c3e50;        /* texto oscuro y elegante */\n"
"    font-size: 20px;        /* tama\u00f1o legible */\n"
"    font-weight: bold;       /* negrita para resaltar */\n"
"    padding: 2px 0;          /* un poco de espacio arriba y abajo */\n"
"}")
        self.lineEdit_24 = QLineEdit(self.page_11)
        self.lineEdit_24.setObjectName(u"lineEdit_24")
        self.lineEdit_24.setGeometry(QRect(240, 110, 261, 51))
        self.lineEdit_24.setFont(font7)
        self.lineEdit_24.setStyleSheet(u"QLineEdit {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #e0e0e0;\n"
"    border-radius: 8px;\n"
"    padding: 6px 10px;\n"
"    font-size: 14px;\n"
"    color: #2c3e50;\n"
"    selection-background-color: #d7e9ff; /* color del texto seleccionado */\n"
"    selection-color: #0b3d91;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #3498db;  /* azul suave al enfocar */\n"
"    background-color: #f9fcff;\n"
"    outline: none;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: #f0f0f0;\n"
"    color: #a0a0a0;\n"
"    border: 2px solid #d0d0d0;\n"
"}")
        self.lineEdit_26 = QLineEdit(self.page_11)
        self.lineEdit_26.setObjectName(u"lineEdit_26")
        self.lineEdit_26.setGeometry(QRect(370, 270, 211, 41))
        self.lineEdit_26.setFont(font7)
        self.lineEdit_26.setStyleSheet(u"QLineEdit {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #e0e0e0;\n"
"    border-radius: 8px;\n"
"    padding: 6px 10px;\n"
"    font-size: 14px;\n"
"    color: #2c3e50;\n"
"    selection-background-color: #d7e9ff; /* color del texto seleccionado */\n"
"    selection-color: #0b3d91;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #3498db;  /* azul suave al enfocar */\n"
"    background-color: #f9fcff;\n"
"    outline: none;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: #f0f0f0;\n"
"    color: #a0a0a0;\n"
"    border: 2px solid #d0d0d0;\n"
"}")
        self.lineEdit_26.setReadOnly(True)
        self.pushButton_8 = QPushButton(self.page_11)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(530, 110, 181, 51))
        self.pushButton_8.setFont(font2)
        self.pushButton_8.setStyleSheet(u"QPushButton:disabled {\n"
"    background-color: #bdc3c7;   /* gris apagado */\n"
"    color: #7f8c8d;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    padding: 10px 20px;\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:enabled {\n"
"    background-color: #2980b9;   /* azul arm\u00f3nico */\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    padding: 10px 20px;\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:enabled:hover {\n"
"    background-color: #3498db;   /* azul m\u00e1s claro */\n"
"}\n"
"\n"
"QPushButton:enabled:pressed {\n"
"    background-color: #1E1E63;   /* azul m\u00e1s oscuro */\n"
"}")
        self.pushButton_15 = QPushButton(self.page_11)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setGeometry(QRect(380, 360, 181, 81))
        self.pushButton_15.setFont(font2)
        self.pushButton_15.setStyleSheet(u"QPushButton:disabled {\n"
"    background-color: #bdc3c7;   /* gris apagado */\n"
"    color: #7f8c8d;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    padding: 10px 20px;\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:enabled {\n"
"    background-color: #2980b9;   /* azul arm\u00f3nico */\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    padding: 10px 20px;\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:enabled:hover {\n"
"    background-color: #3498db;   /* azul m\u00e1s claro */\n"
"}\n"
"\n"
"QPushButton:enabled:pressed {\n"
"    background-color: #2D9623;   /* azul m\u00e1s oscuro */\n"
"}")
        self.label_51 = QLabel(self.page_11)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setGeometry(QRect(0, 10, 961, 91))
        self.label_51.setFont(font2)
        self.label_51.setStyleSheet(u"QLabel {\n"
"    font-size: 26px;           /* m\u00e1s grande */\n"
"    font-weight: bold;\n"
"    color: #3498db;            /* azul destacado */\n"
"    padding: 10px 14px;\n"
"    border-left: 5px solid #3498db;  /* l\u00ednea lateral m\u00e1s gruesa */\n"
"    background-color: #f0f8ff;       /* fondo sutil opcional */\n"
"    margin-bottom: 12px;\n"
"}")
        self.stackedWidget.addWidget(self.page_11)
        self.page_12 = QWidget()
        self.page_12.setObjectName(u"page_12")
        self.label_52 = QLabel(self.page_12)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setGeometry(QRect(0, 0, 961, 101))
        self.label_52.setFont(font2)
        self.label_52.setStyleSheet(u"QLabel {\n"
"    font-size: 26px;           /* m\u00e1s grande */\n"
"    font-weight: bold;\n"
"    color: #3498db;            /* azul destacado */\n"
"    padding: 10px 14px;\n"
"    border-left: 5px solid #3498db;  /* l\u00ednea lateral m\u00e1s gruesa */\n"
"    background-color: #f0f8ff;       /* fondo sutil opcional */\n"
"    margin-bottom: 12px;\n"
"}")
        self.label_16 = QLabel(self.page_12)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(230, 110, 91, 31))
        self.label_16.setFont(font2)
        self.label_16.setStyleSheet(u"QLabel {\n"
"    color: #2c3e50;        /* texto oscuro y elegante */\n"
"    font-size: 20px;        /* tama\u00f1o legible */\n"
"    font-weight: bold;       /* negrita para resaltar */\n"
"    padding: 2px 0;          /* un poco de espacio arriba y abajo */\n"
"}")
        self.label_53 = QLabel(self.page_12)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setGeometry(QRect(230, 160, 91, 31))
        self.label_53.setFont(font2)
        self.label_53.setStyleSheet(u"QLabel {\n"
"    color: #2c3e50;        /* texto oscuro y elegante */\n"
"    font-size: 20px;        /* tama\u00f1o legible */\n"
"    font-weight: bold;       /* negrita para resaltar */\n"
"    padding: 2px 0;          /* un poco de espacio arriba y abajo */\n"
"}")
        self.label_54 = QLabel(self.page_12)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setGeometry(QRect(240, 210, 81, 31))
        self.label_54.setFont(font2)
        self.label_54.setStyleSheet(u"QLabel {\n"
"    color: #2c3e50;        /* texto oscuro y elegante */\n"
"    font-size: 20px;        /* tama\u00f1o legible */\n"
"    font-weight: bold;       /* negrita para resaltar */\n"
"    padding: 2px 0;          /* un poco de espacio arriba y abajo */\n"
"}")
        self.label_55 = QLabel(self.page_12)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setGeometry(QRect(170, 255, 161, 31))
        self.label_55.setFont(font2)
        self.label_55.setStyleSheet(u"QLabel {\n"
"    color: #2c3e50;        /* texto oscuro y elegante */\n"
"    font-size: 20px;        /* tama\u00f1o legible */\n"
"    font-weight: bold;       /* negrita para resaltar */\n"
"    padding: 2px 0;          /* un poco de espacio arriba y abajo */\n"
"}")
        self.label_56 = QLabel(self.page_12)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setGeometry(QRect(150, 370, 171, 41))
        self.label_56.setFont(font2)
        self.label_56.setStyleSheet(u"QLabel {\n"
"    color: #2c3e50;        /* texto oscuro y elegante */\n"
"    font-size: 20px;        /* tama\u00f1o legible */\n"
"    font-weight: bold;       /* negrita para resaltar */\n"
"    padding: 2px 0;          /* un poco de espacio arriba y abajo */\n"
"}")
        self.label_57 = QLabel(self.page_12)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setGeometry(QRect(260, 430, 61, 31))
        self.label_57.setFont(font2)
        self.label_57.setStyleSheet(u"QLabel {\n"
"    color: #2c3e50;        /* texto oscuro y elegante */\n"
"    font-size: 20px;        /* tama\u00f1o legible */\n"
"    font-weight: bold;       /* negrita para resaltar */\n"
"    padding: 2px 0;          /* un poco de espacio arriba y abajo */\n"
"}")
        self.lineEdit_29 = QLineEdit(self.page_12)
        self.lineEdit_29.setObjectName(u"lineEdit_29")
        self.lineEdit_29.setGeometry(QRect(340, 110, 371, 31))
        self.lineEdit_29.setFont(font7)
        self.lineEdit_29.setStyleSheet(u"QLineEdit {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #e0e0e0;\n"
"    border-radius: 8px;\n"
"    padding: 6px 10px;\n"
"    font-size: 14px;\n"
"    color: #2c3e50;\n"
"    selection-background-color: #d7e9ff; /* color del texto seleccionado */\n"
"    selection-color: #0b3d91;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #3498db;  /* azul suave al enfocar */\n"
"    background-color: #f9fcff;\n"
"    outline: none;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: #f0f0f0;\n"
"    color: #a0a0a0;\n"
"    border: 2px solid #d0d0d0;\n"
"}")
        self.lineEdit_30 = QLineEdit(self.page_12)
        self.lineEdit_30.setObjectName(u"lineEdit_30")
        self.lineEdit_30.setGeometry(QRect(340, 160, 371, 31))
        self.lineEdit_30.setFont(font7)
        self.lineEdit_30.setStyleSheet(u"QLineEdit {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #e0e0e0;\n"
"    border-radius: 8px;\n"
"    padding: 6px 10px;\n"
"    font-size: 14px;\n"
"    color: #2c3e50;\n"
"    selection-background-color: #d7e9ff; /* color del texto seleccionado */\n"
"    selection-color: #0b3d91;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #3498db;  /* azul suave al enfocar */\n"
"    background-color: #f9fcff;\n"
"    outline: none;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: #f0f0f0;\n"
"    color: #a0a0a0;\n"
"    border: 2px solid #d0d0d0;\n"
"}")
        self.lineEdit_31 = QLineEdit(self.page_12)
        self.lineEdit_31.setObjectName(u"lineEdit_31")
        self.lineEdit_31.setGeometry(QRect(340, 210, 371, 31))
        self.lineEdit_31.setFont(font7)
        self.lineEdit_31.setStyleSheet(u"QLineEdit {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #e0e0e0;\n"
"    border-radius: 8px;\n"
"    padding: 6px 10px;\n"
"    font-size: 14px;\n"
"    color: #2c3e50;\n"
"    selection-background-color: #d7e9ff; /* color del texto seleccionado */\n"
"    selection-color: #0b3d91;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #3498db;  /* azul suave al enfocar */\n"
"    background-color: #f9fcff;\n"
"    outline: none;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: #f0f0f0;\n"
"    color: #a0a0a0;\n"
"    border: 2px solid #d0d0d0;\n"
"}")
        self.lineEdit_32 = QLineEdit(self.page_12)
        self.lineEdit_32.setObjectName(u"lineEdit_32")
        self.lineEdit_32.setGeometry(QRect(340, 430, 371, 31))
        self.lineEdit_32.setFont(font7)
        self.lineEdit_32.setStyleSheet(u"QLineEdit {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #e0e0e0;\n"
"    border-radius: 8px;\n"
"    padding: 6px 10px;\n"
"    font-size: 14px;\n"
"    color: #2c3e50;\n"
"    selection-background-color: #d7e9ff; /* color del texto seleccionado */\n"
"    selection-color: #0b3d91;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #3498db;  /* azul suave al enfocar */\n"
"    background-color: #f9fcff;\n"
"    outline: none;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: #f0f0f0;\n"
"    color: #a0a0a0;\n"
"    border: 2px solid #d0d0d0;\n"
"}")
        self.pushButton_16 = QPushButton(self.page_12)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setGeometry(QRect(370, 560, 211, 81))
        self.pushButton_16.setFont(font2)
        self.pushButton_16.setStyleSheet(u"QPushButton:disabled {\n"
"    background-color: #bdc3c7;   /* gris apagado */\n"
"    color: #7f8c8d;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    padding: 10px 20px;\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:enabled {\n"
"    background-color: #2980b9;   /* azul arm\u00f3nico */\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    padding: 10px 20px;\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:enabled:hover {\n"
"    background-color: #3498db;   /* azul m\u00e1s claro */\n"
"}\n"
"\n"
"QPushButton:enabled:pressed {\n"
"    background-color: #2D9623;   /* azul m\u00e1s oscuro */\n"
"}")
        self.comboBox_7 = QComboBox(self.page_12)
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.setObjectName(u"comboBox_7")
        self.comboBox_7.setGeometry(QRect(340, 380, 371, 31))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_7.sizePolicy().hasHeightForWidth())
        self.comboBox_7.setSizePolicy(sizePolicy)
        self.comboBox_7.setFont(font7)
        self.comboBox_7.setMouseTracking(True)
        self.comboBox_7.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.comboBox_7.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.comboBox_7.setStyleSheet(u"QComboBox {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #e0e0e0;\n"
"    border-radius: 8px;\n"
"    padding: 6px 10px;\n"
"    font-size: 14px;\n"
"    color: #2c3e50;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 2px solid #b0c4de;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 2px solid #3498db;\n"
"    background-color: #f9fcff;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 24px;\n"
"    border-left: 1px solid #e0e0e0;\n"
"    border-top-right-radius: 6px;\n"
"    border-bottom-right-radius: 6px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* === ESTILO DEL DESPLEGABLE === */\n"
"QComboBox QAbstractItemView {\n"
"    background: #ffffff;\n"
"    border: 1px solid #e0e0e0;\n"
"    border-radius: 8px;\n"
"    padding: 4px;\n"
"    outline: 0;\n"
"    selection-background-color: #d7e9ff;\n"
"    selection-color: #0b3d91;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"    padding: 6px 10px;\n"
""
                        "}\n"
"\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background: #f5faff;\n"
"}")
        self.comboBox_8 = QComboBox(self.page_12)
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.setObjectName(u"comboBox_8")
        self.comboBox_8.setGeometry(QRect(340, 260, 371, 31))
        sizePolicy.setHeightForWidth(self.comboBox_8.sizePolicy().hasHeightForWidth())
        self.comboBox_8.setSizePolicy(sizePolicy)
        self.comboBox_8.setFont(font7)
        self.comboBox_8.setMouseTracking(True)
        self.comboBox_8.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.comboBox_8.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.comboBox_8.setStyleSheet(u"QComboBox {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #e0e0e0;\n"
"    border-radius: 8px;\n"
"    padding: 6px 10px;\n"
"    font-size: 14px;\n"
"    color: #2c3e50;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 2px solid #b0c4de;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 2px solid #3498db;\n"
"    background-color: #f9fcff;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 24px;\n"
"    border-left: 1px solid #e0e0e0;\n"
"    border-top-right-radius: 6px;\n"
"    border-bottom-right-radius: 6px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* === ESTILO DEL DESPLEGABLE === */\n"
"QComboBox QAbstractItemView {\n"
"    background: #ffffff;\n"
"    border: 1px solid #e0e0e0;\n"
"    border-radius: 8px;\n"
"    padding: 4px;\n"
"    outline: 0;\n"
"    selection-background-color: #d7e9ff;\n"
"    selection-color: #0b3d91;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"    padding: 6px 10px;\n"
""
                        "}\n"
"\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background: #f5faff;\n"
"}")
        self.comboBox_9 = QComboBox(self.page_12)
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.setObjectName(u"comboBox_9")
        self.comboBox_9.setGeometry(QRect(340, 325, 371, 31))
        sizePolicy.setHeightForWidth(self.comboBox_9.sizePolicy().hasHeightForWidth())
        self.comboBox_9.setSizePolicy(sizePolicy)
        self.comboBox_9.setFont(font7)
        self.comboBox_9.setMouseTracking(True)
        self.comboBox_9.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.comboBox_9.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.comboBox_9.setStyleSheet(u"QComboBox {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #e0e0e0;\n"
"    border-radius: 8px;\n"
"    padding: 6px 10px;\n"
"    font-size: 14px;\n"
"    color: #2c3e50;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 2px solid #b0c4de;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 2px solid #3498db;\n"
"    background-color: #f9fcff;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 24px;\n"
"    border-left: 1px solid #e0e0e0;\n"
"    border-top-right-radius: 6px;\n"
"    border-bottom-right-radius: 6px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* === ESTILO DEL DESPLEGABLE === */\n"
"QComboBox QAbstractItemView {\n"
"    background: #ffffff;\n"
"    border: 1px solid #e0e0e0;\n"
"    border-radius: 8px;\n"
"    padding: 4px;\n"
"    outline: 0;\n"
"    selection-background-color: #d7e9ff;\n"
"    selection-color: #0b3d91;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"    padding: 6px 10px;\n"
""
                        "}\n"
"\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background: #f5faff;\n"
"}")
        self.label_58 = QLabel(self.page_12)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setGeometry(QRect(160, 320, 171, 31))
        self.label_58.setFont(font2)
        self.label_58.setStyleSheet(u"QLabel {\n"
"    color: #2c3e50;        /* texto oscuro y elegante */\n"
"    font-size: 20px;        /* tama\u00f1o legible */\n"
"    font-weight: bold;       /* negrita para resaltar */\n"
"    padding: 2px 0;          /* un poco de espacio arriba y abajo */\n"
"}")
        self.lineEdit = QLineEdit(self.page_12)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(400, 480, 161, 51))
        self.lineEdit.setFont(font2)
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #e0e0e0;\n"
"    border-radius: 8px;\n"
"    padding: 6px 10px;\n"
"    font-size: 14px;\n"
"    color: #2c3e50;\n"
"    selection-background-color: #d7e9ff; /* color del texto seleccionado */\n"
"    selection-color: #0b3d91;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #3498db;  /* azul suave al enfocar */\n"
"    background-color: #f9fcff;\n"
"    outline: none;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: #f0f0f0;\n"
"    color: #a0a0a0;\n"
"    border: 2px solid #d0d0d0;\n"
"}")
        self.lineEdit.setReadOnly(True)
        self.label_4 = QLabel(self.page_12)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(270, 480, 81, 41))
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"QLabel {\n"
"    color: #2c3e50;        /* texto oscuro y elegante */\n"
"    font-size: 20px;        /* tama\u00f1o legible */\n"
"    font-weight: bold;       /* negrita para resaltar */\n"
"    padding: 2px 0;          /* un poco de espacio arriba y abajo */\n"
"}")
        self.stackedWidget.addWidget(self.page_12)
        self.page_13 = QWidget()
        self.page_13.setObjectName(u"page_13")
        self.label_59 = QLabel(self.page_13)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setGeometry(QRect(270, 170, 391, 31))
        self.label_59.setFont(font2)
        self.label_59.setStyleSheet(u"QLabel {\n"
"    color: #2c3e50;        /* texto oscuro y elegante */\n"
"    font-size: 20px;        /* tama\u00f1o legible */\n"
"    font-weight: bold;       /* negrita para resaltar */\n"
"    padding: 2px 0;          /* un poco de espacio arriba y abajo */\n"
"}")
        self.label_60 = QLabel(self.page_13)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setGeometry(QRect(0, 0, 971, 101))
        self.label_60.setFont(font2)
        self.label_60.setStyleSheet(u"QLabel {\n"
"    font-size: 26px;           /* m\u00e1s grande */\n"
"    font-weight: bold;\n"
"    color: #3498db;            /* azul destacado */\n"
"    padding: 10px 14px;\n"
"    border-left: 5px solid #3498db;  /* l\u00ednea lateral m\u00e1s gruesa */\n"
"    background-color: #f0f8ff;       /* fondo sutil opcional */\n"
"    margin-bottom: 12px;\n"
"}")
        self.lineEdit_33 = QLineEdit(self.page_13)
        self.lineEdit_33.setObjectName(u"lineEdit_33")
        self.lineEdit_33.setGeometry(QRect(200, 110, 261, 41))
        self.lineEdit_33.setFont(font7)
        self.lineEdit_33.setStyleSheet(u"QLineEdit {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #e0e0e0;\n"
"    border-radius: 8px;\n"
"    padding: 6px 10px;\n"
"    font-size: 14px;\n"
"    color: #2c3e50;\n"
"    selection-background-color: #d7e9ff; /* color del texto seleccionado */\n"
"    selection-color: #0b3d91;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #3498db;  /* azul suave al enfocar */\n"
"    background-color: #f9fcff;\n"
"    outline: none;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: #f0f0f0;\n"
"    color: #a0a0a0;\n"
"    border: 2px solid #d0d0d0;\n"
"}")
        self.pushButton_17 = QPushButton(self.page_13)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setGeometry(QRect(520, 100, 161, 51))
        self.pushButton_17.setFont(font2)
        self.pushButton_17.setStyleSheet(u"QPushButton:disabled {\n"
"    background-color: #bdc3c7;   /* gris apagado */\n"
"    color: #7f8c8d;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    padding: 10px 20px;\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:enabled {\n"
"    background-color: #2980b9;   /* azul arm\u00f3nico */\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    padding: 10px 20px;\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:enabled:hover {\n"
"    background-color: #3498db;   /* azul m\u00e1s claro */\n"
"}\n"
"\n"
"QPushButton:enabled:pressed {\n"
"    background-color: #D11515;   /* azul m\u00e1s oscuro */\n"
"}")
        self.plainTextEdit_3 = QPlainTextEdit(self.page_13)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")
        self.plainTextEdit_3.setGeometry(QRect(210, 210, 521, 301))
        self.plainTextEdit_3.setFont(font7)
        self.plainTextEdit_3.setStyleSheet(u"QPlainTextEdit {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #e0e0e0;\n"
"    border-radius: 8px;\n"
"    padding: 8px;\n"
"    font-size: 14px;\n"
"    color: #2c3e50;\n"
"    selection-background-color: #3498db;\n"
"    selection-color: white;\n"
"}\n"
"\n"
"QPlainTextEdit:hover {\n"
"    border: 2px solid #b0c4de;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border: 2px solid #3498db;\n"
"    background-color: #f9fcff;\n"
"    outline: none;\n"
"}\n"
"\n"
"/* Scrollbar vertical */\n"
"QPlainTextEdit QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #f0f0f0;\n"
"    width: 10px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPlainTextEdit QScrollBar::handle:vertical {\n"
"    background: #b0c4de;\n"
"    min-height: 20px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPlainTextEdit QScrollBar::handle:vertical:hover {\n"
"    background: #3498db;\n"
"}\n"
"\n"
"QPlainTextEdit QScrollBar::add-line, QPlainTextEdit QScrollBar::sub-line {\n"
"    height: 0;\n"
"}")
        self.stackedWidget.addWidget(self.page_13)
        self.page_14 = QWidget()
        self.page_14.setObjectName(u"page_14")
        self.label_61 = QLabel(self.page_14)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setGeometry(QRect(0, 20, 961, 91))
        self.label_61.setFont(font2)
        self.label_61.setStyleSheet(u"QLabel {\n"
"    font-size: 26px;           /* m\u00e1s grande */\n"
"    font-weight: bold;\n"
"    color: #3498db;            /* azul destacado */\n"
"    padding: 10px 14px;\n"
"    border-left: 5px solid #3498db;  /* l\u00ednea lateral m\u00e1s gruesa */\n"
"    background-color: #f0f8ff;       /* fondo sutil opcional */\n"
"    margin-bottom: 12px;\n"
"}")
        self.lineEdit_34 = QLineEdit(self.page_14)
        self.lineEdit_34.setObjectName(u"lineEdit_34")
        self.lineEdit_34.setGeometry(QRect(340, 130, 371, 31))
        self.lineEdit_34.setFont(font7)
        self.lineEdit_34.setStyleSheet(u"QLineEdit {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #e0e0e0;\n"
"    border-radius: 8px;\n"
"    padding: 6px 10px;\n"
"    font-size: 14px;\n"
"    color: #2c3e50;\n"
"    selection-background-color: #d7e9ff; /* color del texto seleccionado */\n"
"    selection-color: #0b3d91;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #3498db;  /* azul suave al enfocar */\n"
"    background-color: #f9fcff;\n"
"    outline: none;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: #f0f0f0;\n"
"    color: #a0a0a0;\n"
"    border: 2px solid #d0d0d0;\n"
"}")
        self.comboBox_10 = QComboBox(self.page_14)
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.setObjectName(u"comboBox_10")
        self.comboBox_10.setGeometry(QRect(340, 280, 371, 31))
        sizePolicy.setHeightForWidth(self.comboBox_10.sizePolicy().hasHeightForWidth())
        self.comboBox_10.setSizePolicy(sizePolicy)
        self.comboBox_10.setFont(font7)
        self.comboBox_10.setMouseTracking(True)
        self.comboBox_10.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.comboBox_10.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.comboBox_10.setStyleSheet(u"QComboBox {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #e0e0e0;\n"
"    border-radius: 8px;\n"
"    padding: 6px 10px;\n"
"    font-size: 14px;\n"
"    color: #2c3e50;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 2px solid #b0c4de;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 2px solid #3498db;\n"
"    background-color: #f9fcff;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 24px;\n"
"    border-left: 1px solid #e0e0e0;\n"
"    border-top-right-radius: 6px;\n"
"    border-bottom-right-radius: 6px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* === ESTILO DEL DESPLEGABLE === */\n"
"QComboBox QAbstractItemView {\n"
"    background: #ffffff;\n"
"    border: 1px solid #e0e0e0;\n"
"    border-radius: 8px;\n"
"    padding: 4px;\n"
"    outline: 0;\n"
"    selection-background-color: #d7e9ff;\n"
"    selection-color: #0b3d91;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"    padding: 6px 10px;\n"
""
                        "}\n"
"\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background: #f5faff;\n"
"}")
        self.label_62 = QLabel(self.page_14)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setGeometry(QRect(200, 180, 111, 31))
        self.label_62.setFont(font2)
        self.label_62.setStyleSheet(u"QLabel {\n"
"    color: #2c3e50;        /* texto oscuro y elegante */\n"
"    font-size: 20px;        /* tama\u00f1o legible */\n"
"    font-weight: bold;       /* negrita para resaltar */\n"
"    padding: 2px 0;          /* un poco de espacio arriba y abajo */\n"
"}")
        self.label_63 = QLabel(self.page_14)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setGeometry(QRect(140, 240, 191, 20))
        self.label_63.setFont(font2)
        self.label_63.setStyleSheet(u"QLabel {\n"
"    color: #2c3e50;        /* texto oscuro y elegante */\n"
"    font-size: 20px;        /* tama\u00f1o legible */\n"
"    font-weight: bold;       /* negrita para resaltar */\n"
"    padding: 2px 0;          /* un poco de espacio arriba y abajo */\n"
"}")
        self.label_17 = QLabel(self.page_14)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(230, 130, 91, 31))
        self.label_17.setFont(font2)
        self.label_17.setStyleSheet(u"QLabel {\n"
"    color: #2c3e50;        /* texto oscuro y elegante */\n"
"    font-size: 20px;        /* tama\u00f1o legible */\n"
"    font-weight: bold;       /* negrita para resaltar */\n"
"    padding: 2px 0;          /* un poco de espacio arriba y abajo */\n"
"}")
        self.lineEdit_35 = QLineEdit(self.page_14)
        self.lineEdit_35.setObjectName(u"lineEdit_35")
        self.lineEdit_35.setGeometry(QRect(340, 180, 371, 31))
        self.lineEdit_35.setFont(font7)
        self.lineEdit_35.setStyleSheet(u"QLineEdit {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #e0e0e0;\n"
"    border-radius: 8px;\n"
"    padding: 6px 10px;\n"
"    font-size: 14px;\n"
"    color: #2c3e50;\n"
"    selection-background-color: #d7e9ff; /* color del texto seleccionado */\n"
"    selection-color: #0b3d91;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #3498db;  /* azul suave al enfocar */\n"
"    background-color: #f9fcff;\n"
"    outline: none;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: #f0f0f0;\n"
"    color: #a0a0a0;\n"
"    border: 2px solid #d0d0d0;\n"
"}")
        self.lineEdit_36 = QLineEdit(self.page_14)
        self.lineEdit_36.setObjectName(u"lineEdit_36")
        self.lineEdit_36.setGeometry(QRect(340, 230, 371, 31))
        self.lineEdit_36.setFont(font7)
        self.lineEdit_36.setStyleSheet(u"QLineEdit {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #e0e0e0;\n"
"    border-radius: 8px;\n"
"    padding: 6px 10px;\n"
"    font-size: 14px;\n"
"    color: #2c3e50;\n"
"    selection-background-color: #d7e9ff; /* color del texto seleccionado */\n"
"    selection-color: #0b3d91;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #3498db;  /* azul suave al enfocar */\n"
"    background-color: #f9fcff;\n"
"    outline: none;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: #f0f0f0;\n"
"    color: #a0a0a0;\n"
"    border: 2px solid #d0d0d0;\n"
"}")
        self.label_64 = QLabel(self.page_14)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setGeometry(QRect(160, 279, 161, 31))
        self.label_64.setFont(font2)
        self.label_64.setStyleSheet(u"QLabel {\n"
"    color: #2c3e50;        /* texto oscuro y elegante */\n"
"    font-size: 20px;        /* tama\u00f1o legible */\n"
"    font-weight: bold;       /* negrita para resaltar */\n"
"    padding: 2px 0;          /* un poco de espacio arriba y abajo */\n"
"}")
        self.pushButton_18 = QPushButton(self.page_14)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setGeometry(QRect(350, 350, 241, 91))
        self.pushButton_18.setFont(font2)
        self.pushButton_18.setStyleSheet(u"QPushButton:disabled {\n"
"    background-color: #bdc3c7;   /* gris apagado */\n"
"    color: #7f8c8d;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    padding: 10px 20px;\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:enabled {\n"
"    background-color: #2980b9;   /* azul arm\u00f3nico */\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    padding: 10px 20px;\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:enabled:hover {\n"
"    background-color: #3498db;   /* azul m\u00e1s claro */\n"
"}\n"
"\n"
"QPushButton:enabled:pressed {\n"
"    background-color: #2D9623;   /* azul m\u00e1s oscuro */\n"
"}")
        self.stackedWidget.addWidget(self.page_14)
        self.page_15 = QWidget()
        self.page_15.setObjectName(u"page_15")
        self.label_65 = QLabel(self.page_15)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setGeometry(QRect(0, 20, 971, 101))
        self.label_65.setFont(font2)
        self.label_65.setStyleSheet(u"QLabel {\n"
"    font-size: 26px;           /* m\u00e1s grande */\n"
"    font-weight: bold;\n"
"    color: #3498db;            /* azul destacado */\n"
"    padding: 10px 14px;\n"
"    border-left: 5px solid #3498db;  /* l\u00ednea lateral m\u00e1s gruesa */\n"
"    background-color: #f0f8ff;       /* fondo sutil opcional */\n"
"    margin-bottom: 12px;\n"
"}")
        self.pushButton_19 = QPushButton(self.page_15)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setGeometry(QRect(330, 490, 221, 91))
        self.pushButton_19.setFont(font2)
        self.pushButton_19.setStyleSheet(u"QPushButton:disabled {\n"
"    background-color: #bdc3c7;   /* gris apagado */\n"
"    color: #7f8c8d;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    padding: 10px 20px;\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:enabled {\n"
"    background-color: #2980b9;   /* azul arm\u00f3nico */\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    padding: 10px 20px;\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:enabled:hover {\n"
"    background-color: #3498db;   /* azul m\u00e1s claro */\n"
"}\n"
"\n"
"QPushButton:enabled:pressed {\n"
"    background-color: #1f618d;   /* azul m\u00e1s oscuro */\n"
"}")
        self.label_66 = QLabel(self.page_15)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setGeometry(QRect(260, 249, 131, 31))
        self.label_66.setFont(font2)
        self.label_66.setStyleSheet(u"QLabel {\n"
"    color: #2c3e50;        /* texto oscuro y elegante */\n"
"    font-size: 20px;        /* tama\u00f1o legible */\n"
"    font-weight: bold;       /* negrita para resaltar */\n"
"    padding: 2px 0;          /* un poco de espacio arriba y abajo */\n"
"}")
        self.label_67 = QLabel(self.page_15)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setGeometry(QRect(260, 200, 131, 31))
        self.label_67.setFont(font2)
        self.label_67.setStyleSheet(u"QLabel {\n"
"    color: #2c3e50;        /* texto oscuro y elegante */\n"
"    font-size: 20px;        /* tama\u00f1o legible */\n"
"    font-weight: bold;       /* negrita para resaltar */\n"
"    padding: 2px 0;          /* un poco de espacio arriba y abajo */\n"
"}")
        self.label_18 = QLabel(self.page_15)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(220, 150, 171, 31))
        self.label_18.setFont(font2)
        self.label_18.setStyleSheet(u"QLabel {\n"
"    color: #2c3e50;        /* texto oscuro y elegante */\n"
"    font-size: 20px;        /* tama\u00f1o legible */\n"
"    font-weight: bold;       /* negrita para resaltar */\n"
"    padding: 2px 0;          /* un poco de espacio arriba y abajo */\n"
"}")
        self.label_68 = QLabel(self.page_15)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setGeometry(QRect(230, 290, 151, 31))
        self.label_68.setFont(font2)
        self.label_68.setStyleSheet(u"QLabel {\n"
"    color: #2c3e50;        /* texto oscuro y elegante */\n"
"    font-size: 20px;        /* tama\u00f1o legible */\n"
"    font-weight: bold;       /* negrita para resaltar */\n"
"    padding: 2px 0;          /* un poco de espacio arriba y abajo */\n"
"}")
        self.label_69 = QLabel(self.page_15)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setGeometry(QRect(270, 340, 121, 31))
        self.label_69.setFont(font2)
        self.label_69.setStyleSheet(u"QLabel {\n"
"    color: #2c3e50;        /* texto oscuro y elegante */\n"
"    font-size: 20px;        /* tama\u00f1o legible */\n"
"    font-weight: bold;       /* negrita para resaltar */\n"
"    padding: 2px 0;          /* un poco de espacio arriba y abajo */\n"
"}")
        self.label_70 = QLabel(self.page_15)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setGeometry(QRect(270, 389, 121, 31))
        self.label_70.setFont(font2)
        self.label_70.setStyleSheet(u"QLabel {\n"
"    color: #2c3e50;        /* texto oscuro y elegante */\n"
"    font-size: 20px;        /* tama\u00f1o legible */\n"
"    font-weight: bold;       /* negrita para resaltar */\n"
"    padding: 2px 0;          /* un poco de espacio arriba y abajo */\n"
"}")
        self.comboBox_11 = QComboBox(self.page_15)
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.setObjectName(u"comboBox_11")
        self.comboBox_11.setGeometry(QRect(410, 150, 371, 31))
        sizePolicy.setHeightForWidth(self.comboBox_11.sizePolicy().hasHeightForWidth())
        self.comboBox_11.setSizePolicy(sizePolicy)
        self.comboBox_11.setFont(font7)
        self.comboBox_11.setMouseTracking(True)
        self.comboBox_11.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.comboBox_11.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.comboBox_11.setStyleSheet(u"QComboBox {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #e0e0e0;\n"
"    border-radius: 8px;\n"
"    padding: 6px 10px;\n"
"    font-size: 14px;\n"
"    color: #2c3e50;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 2px solid #b0c4de;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 2px solid #3498db;\n"
"    background-color: #f9fcff;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 24px;\n"
"    border-left: 1px solid #e0e0e0;\n"
"    border-top-right-radius: 6px;\n"
"    border-bottom-right-radius: 6px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* === ESTILO DEL DESPLEGABLE === */\n"
"QComboBox QAbstractItemView {\n"
"    background: #ffffff;\n"
"    border: 1px solid #e0e0e0;\n"
"    border-radius: 8px;\n"
"    padding: 4px;\n"
"    outline: 0;\n"
"    selection-background-color: #d7e9ff;\n"
"    selection-color: #0b3d91;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"    padding: 6px 10px;\n"
""
                        "}\n"
"\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background: #f5faff;\n"
"}")
        self.doubleSpinBox_5 = QDoubleSpinBox(self.page_15)
        self.doubleSpinBox_5.setObjectName(u"doubleSpinBox_5")
        self.doubleSpinBox_5.setGeometry(QRect(410, 250, 371, 31))
        self.doubleSpinBox_5.setFont(font7)
        self.doubleSpinBox_5.setStyleSheet(u"QDoubleSpinBox {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #e0e0e0;\n"
"    border-radius: 8px;\n"
"    padding: 4px 8px;\n"
"    font-size: 14px;\n"
"    color: #2c3e50;\n"
"}\n"
"\n"
"QDoubleSpinBox:hover {\n"
"    border: 2px solid #b0c4de;\n"
"}\n"
"\n"
"QDoubleSpinBox:focus {\n"
"    border: 2px solid #3498db;\n"
"    background-color: #f9fcff;\n"
"    outline: none;\n"
"}\n"
"\n"
"/* Botones de incremento/decremento */\n"
"QDoubleSpinBox::up-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    border-left: 1px solid #e0e0e0;\n"
"    background-color: #f0f0f0;\n"
"    border-top-right-radius: 6px;\n"
"}\n"
"\n"
"QDoubleSpinBox::up-button:hover {\n"
"    background-color: #d7e9ff;\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: bottom right;\n"
"    width: 20px;\n"
"    border-left: 1px solid #e0e0e0;\n"
"    background-color: #f0f0f0;\n"
"    border-bottom-right-radiu"
                        "s: 6px;\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button:hover {\n"
"    background-color: #d7e9ff;\n"
"}\n"
"\n"
"/* Flechas */\n"
"QDoubleSpinBox::up-arrow {\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"\n"
"QDoubleSpinBox::down-arrow {\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}")
        self.doubleSpinBox_5.setMaximum(9999.000000000000000)
        self.doubleSpinBox_6 = QDoubleSpinBox(self.page_15)
        self.doubleSpinBox_6.setObjectName(u"doubleSpinBox_6")
        self.doubleSpinBox_6.setGeometry(QRect(410, 290, 371, 31))
        self.doubleSpinBox_6.setFont(font7)
        self.doubleSpinBox_6.setStyleSheet(u"QDoubleSpinBox {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #e0e0e0;\n"
"    border-radius: 8px;\n"
"    padding: 4px 8px;\n"
"    font-size: 14px;\n"
"    color: #2c3e50;\n"
"}\n"
"\n"
"QDoubleSpinBox:hover {\n"
"    border: 2px solid #b0c4de;\n"
"}\n"
"\n"
"QDoubleSpinBox:focus {\n"
"    border: 2px solid #3498db;\n"
"    background-color: #f9fcff;\n"
"    outline: none;\n"
"}\n"
"\n"
"/* Botones de incremento/decremento */\n"
"QDoubleSpinBox::up-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    border-left: 1px solid #e0e0e0;\n"
"    background-color: #f0f0f0;\n"
"    border-top-right-radius: 6px;\n"
"}\n"
"\n"
"QDoubleSpinBox::up-button:hover {\n"
"    background-color: #d7e9ff;\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: bottom right;\n"
"    width: 20px;\n"
"    border-left: 1px solid #e0e0e0;\n"
"    background-color: #f0f0f0;\n"
"    border-bottom-right-radiu"
                        "s: 6px;\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button:hover {\n"
"    background-color: #d7e9ff;\n"
"}\n"
"\n"
"/* Flechas */\n"
"QDoubleSpinBox::up-arrow {\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"\n"
"QDoubleSpinBox::down-arrow {\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}")
        self.doubleSpinBox_6.setMaximum(9999.989999999999782)
        self.doubleSpinBox_7 = QDoubleSpinBox(self.page_15)
        self.doubleSpinBox_7.setObjectName(u"doubleSpinBox_7")
        self.doubleSpinBox_7.setGeometry(QRect(410, 340, 371, 31))
        self.doubleSpinBox_7.setFont(font7)
        self.doubleSpinBox_7.setStyleSheet(u"QDoubleSpinBox {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #e0e0e0;\n"
"    border-radius: 8px;\n"
"    padding: 4px 8px;\n"
"    font-size: 14px;\n"
"    color: #2c3e50;\n"
"}\n"
"\n"
"QDoubleSpinBox:hover {\n"
"    border: 2px solid #b0c4de;\n"
"}\n"
"\n"
"QDoubleSpinBox:focus {\n"
"    border: 2px solid #3498db;\n"
"    background-color: #f9fcff;\n"
"    outline: none;\n"
"}\n"
"\n"
"/* Botones de incremento/decremento */\n"
"QDoubleSpinBox::up-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    border-left: 1px solid #e0e0e0;\n"
"    background-color: #f0f0f0;\n"
"    border-top-right-radius: 6px;\n"
"}\n"
"\n"
"QDoubleSpinBox::up-button:hover {\n"
"    background-color: #d7e9ff;\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: bottom right;\n"
"    width: 20px;\n"
"    border-left: 1px solid #e0e0e0;\n"
"    background-color: #f0f0f0;\n"
"    border-bottom-right-radiu"
                        "s: 6px;\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button:hover {\n"
"    background-color: #d7e9ff;\n"
"}\n"
"\n"
"/* Flechas */\n"
"QDoubleSpinBox::up-arrow {\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"\n"
"QDoubleSpinBox::down-arrow {\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}")
        self.doubleSpinBox_7.setMaximum(9999.989999999999782)
        self.doubleSpinBox_8 = QDoubleSpinBox(self.page_15)
        self.doubleSpinBox_8.setObjectName(u"doubleSpinBox_8")
        self.doubleSpinBox_8.setGeometry(QRect(410, 390, 371, 31))
        self.doubleSpinBox_8.setFont(font7)
        self.doubleSpinBox_8.setStyleSheet(u"QDoubleSpinBox {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #e0e0e0;\n"
"    border-radius: 8px;\n"
"    padding: 4px 8px;\n"
"    font-size: 14px;\n"
"    color: #2c3e50;\n"
"}\n"
"\n"
"QDoubleSpinBox:hover {\n"
"    border: 2px solid #b0c4de;\n"
"}\n"
"\n"
"QDoubleSpinBox:focus {\n"
"    border: 2px solid #3498db;\n"
"    background-color: #f9fcff;\n"
"    outline: none;\n"
"}\n"
"\n"
"/* Botones de incremento/decremento */\n"
"QDoubleSpinBox::up-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    border-left: 1px solid #e0e0e0;\n"
"    background-color: #f0f0f0;\n"
"    border-top-right-radius: 6px;\n"
"}\n"
"\n"
"QDoubleSpinBox::up-button:hover {\n"
"    background-color: #d7e9ff;\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: bottom right;\n"
"    width: 20px;\n"
"    border-left: 1px solid #e0e0e0;\n"
"    background-color: #f0f0f0;\n"
"    border-bottom-right-radiu"
                        "s: 6px;\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button:hover {\n"
"    background-color: #d7e9ff;\n"
"}\n"
"\n"
"/* Flechas */\n"
"QDoubleSpinBox::up-arrow {\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"\n"
"QDoubleSpinBox::down-arrow {\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}")
        self.doubleSpinBox_8.setMaximum(9999990000.000000000000000)
        self.comboBox_12 = QComboBox(self.page_15)
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.setObjectName(u"comboBox_12")
        self.comboBox_12.setGeometry(QRect(410, 200, 371, 31))
        sizePolicy.setHeightForWidth(self.comboBox_12.sizePolicy().hasHeightForWidth())
        self.comboBox_12.setSizePolicy(sizePolicy)
        self.comboBox_12.setFont(font7)
        self.comboBox_12.setMouseTracking(True)
        self.comboBox_12.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.comboBox_12.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.comboBox_12.setStyleSheet(u"QComboBox {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #e0e0e0;\n"
"    border-radius: 8px;\n"
"    padding: 6px 10px;\n"
"    font-size: 14px;\n"
"    color: #2c3e50;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 2px solid #b0c4de;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 2px solid #3498db;\n"
"    background-color: #f9fcff;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 24px;\n"
"    border-left: 1px solid #e0e0e0;\n"
"    border-top-right-radius: 6px;\n"
"    border-bottom-right-radius: 6px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* === ESTILO DEL DESPLEGABLE === */\n"
"QComboBox QAbstractItemView {\n"
"    background: #ffffff;\n"
"    border: 1px solid #e0e0e0;\n"
"    border-radius: 8px;\n"
"    padding: 4px;\n"
"    outline: 0;\n"
"    selection-background-color: #d7e9ff;\n"
"    selection-color: #0b3d91;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"    padding: 6px 10px;\n"
""
                        "}\n"
"\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background: #f5faff;\n"
"}")
        self.stackedWidget.addWidget(self.page_15)
        self.page_16 = QWidget()
        self.page_16.setObjectName(u"page_16")
        self.label_71 = QLabel(self.page_16)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setGeometry(QRect(-10, 10, 971, 81))
        self.label_71.setFont(font2)
        self.label_71.setStyleSheet(u"QLabel {\n"
"    font-size: 26px;           /* m\u00e1s grande */\n"
"    font-weight: bold;\n"
"    color: #3498db;            /* azul destacado */\n"
"    padding: 10px 14px;\n"
"    border-left: 5px solid #3498db;  /* l\u00ednea lateral m\u00e1s gruesa */\n"
"    background-color: #f0f8ff;       /* fondo sutil opcional */\n"
"    margin-bottom: 12px;\n"
"}")
        self.calendarWidget_5 = QCalendarWidget(self.page_16)
        self.calendarWidget_5.setObjectName(u"calendarWidget_5")
        self.calendarWidget_5.setGeometry(QRect(10, 160, 431, 281))
        self.calendarWidget_5.setFont(font5)
        self.calendarWidget_5.setStyleSheet(u"QCalendarWidget {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #e0e0e0;\n"
"    border-radius: 8px;\n"
"    color: #2c3e50;\n"
"    selection-background-color: #3498db;\n"
"    selection-color: white;\n"
"}\n"
"\n"
"QCalendarWidget QWidget#qt_calendar_navigationbar {\n"
"    background-color: #f0f0f0;\n"
"    border-bottom: 1px solid #e0e0e0;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton {\n"
"    color: #2c3e50;\n"
"    background: transparent;\n"
"    border: none;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton:hover {\n"
"    color: #3498db;\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView {\n"
"    background-color: #ffffff;\n"
"    border: none;\n"
"    selection-background-color: #3498db;\n"
"    selection-color: white;\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView::item {\n"
"    border-radius: 6px;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView::item:hover {\n"
"    background-color: #d7e9ff;\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView"
                        "::item:selected {\n"
"    background-color: #3498db;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"}")
        self.label_72 = QLabel(self.page_16)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setGeometry(QRect(150, 100, 141, 41))
        self.label_72.setFont(font2)
        self.label_72.setStyleSheet(u"QLabel {\n"
"    color: #2c3e50;      /* texto oscuro elegante */\n"
"    font-size: 20px;      /* tama\u00f1o legible */\n"
"    font-weight: bold;    /* negrita */\n"
"    padding: 2px 0;       /* espacio vertical */\n"
"}\n"
"\n"
"QLabel[required=\"true\"] {\n"
"    color: #e74c3c;       /* rojo si es obligatorio */\n"
"    font-weight: bold;\n"
"}")
        self.label_73 = QLabel(self.page_16)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setGeometry(QRect(670, 100, 141, 41))
        self.label_73.setFont(font2)
        self.label_73.setStyleSheet(u"QLabel {\n"
"    color: #2c3e50;      /* texto oscuro elegante */\n"
"    font-size: 20px;      /* tama\u00f1o legible */\n"
"    font-weight: bold;    /* negrita */\n"
"    padding: 2px 0;       /* espacio vertical */\n"
"}\n"
"\n"
"QLabel[required=\"true\"] {\n"
"    color: #e74c3c;       /* rojo si es obligatorio */\n"
"    font-weight: bold;\n"
"}")
        self.pushButton_20 = QPushButton(self.page_16)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setGeometry(QRect(380, 480, 201, 91))
        self.pushButton_20.setFont(font2)
        self.pushButton_20.setStyleSheet(u"QPushButton:disabled {\n"
"    background-color: #bdc3c7;   /* gris apagado */\n"
"    color: #7f8c8d;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    padding: 10px 20px;\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:enabled {\n"
"    background-color: #2980b9;   /* azul arm\u00f3nico */\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    padding: 10px 20px;\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:enabled:hover {\n"
"    background-color: #3498db;   /* azul m\u00e1s claro */\n"
"}\n"
"\n"
"QPushButton:enabled:pressed {\n"
"    background-color: #1f618d;   /* azul m\u00e1s oscuro */\n"
"}")
        self.label_74 = QLabel(self.page_16)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setGeometry(QRect(450, 300, 51, 61))
        self.label_74.setStyleSheet(u"QLabel{\n"
"    font-size: 20px;           /* m\u00e1s grande */\n"
"    font-weight: bold;          /* negrita */\n"
"    color: #3498db;             /* azul destacado */\n"
"    padding: 8px 12px;\n"
"    border-left: 4px solid #3498db;  /* l\u00ednea lateral para \u00e9nfasis */\n"
"    background-color: #f0f8ff;       /* opcional: fondo muy sutil */\n"
"    margin-bottom: 10px;\n"
"}")
        self.label_74.setPixmap(QPixmap(u":/prefijoNuevo/arrow-right.svg"))
        self.label_74.setScaledContents(True)
        self.label_74.setWordWrap(False)
        self.label_74.setMargin(0)
        self.label_74.setIndent(0)
        self.calendarWidget_6 = QCalendarWidget(self.page_16)
        self.calendarWidget_6.setObjectName(u"calendarWidget_6")
        self.calendarWidget_6.setGeometry(QRect(510, 160, 431, 281))
        self.calendarWidget_6.setFont(font5)
        self.calendarWidget_6.setStyleSheet(u"QCalendarWidget {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #e0e0e0;\n"
"    border-radius: 8px;\n"
"    color: #2c3e50;\n"
"    selection-background-color: #3498db;\n"
"    selection-color: white;\n"
"}\n"
"\n"
"QCalendarWidget QWidget#qt_calendar_navigationbar {\n"
"    background-color: #f0f0f0;\n"
"    border-bottom: 1px solid #e0e0e0;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton {\n"
"    color: #2c3e50;\n"
"    background: transparent;\n"
"    border: none;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton:hover {\n"
"    color: #3498db;\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView {\n"
"    background-color: #ffffff;\n"
"    border: none;\n"
"    selection-background-color: #3498db;\n"
"    selection-color: white;\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView::item {\n"
"    border-radius: 6px;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView::item:hover {\n"
"    background-color: #d7e9ff;\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView"
                        "::item:selected {\n"
"    background-color: #3498db;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"}")
        self.stackedWidget.addWidget(self.page_16)

        self.gridLayout_2.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.verticalLayout_8.addWidget(self.main)


        self.horizontalLayout_2.addLayout(self.verticalLayout_8)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.exit_2.toggled.connect(MainWindow.close)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Estacionamiento", None))
        self.add_vehiculo_2.setText(QCoreApplication.translate("MainWindow", u"Agregar Vehiculo", None))
        self.pagar_2.setText(QCoreApplication.translate("MainWindow", u"Pagar Ticket", None))
        self.pagar_ext_3.setText(QCoreApplication.translate("MainWindow", u"Pagar Ticket Extravio", None))
        self.add_pencion_2.setText(QCoreApplication.translate("MainWindow", u"Agregar Pencion", None))
        self.borrar_ticket_2.setText(QCoreApplication.translate("MainWindow", u"Borrar Ticket", None))
        self.label.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Administrador", None))
        self.add_usuario_2.setText(QCoreApplication.translate("MainWindow", u"Agregar Usario", None))
        self.mod_tarifa_2.setText(QCoreApplication.translate("MainWindow", u"Modificar cuotas", None))
        self.reporte_2.setText(QCoreApplication.translate("MainWindow", u"Realizar reporte", None))
        self.exit_2.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
        self.label_usuario_2.setText(QCoreApplication.translate("MainWindow", u"Hola, Omar", None))
        self.label_rol_2.setText(QCoreApplication.translate("MainWindow", u"Bienvenido a la aplicacion de Administrador", None))
#if QT_CONFIG(statustip)
        self.stackedWidget.setStatusTip("")
#endif // QT_CONFIG(statustip)
        ___qtablewidgetitem = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Id_ticket", None));
        ___qtablewidgetitem1 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Codigo barras", None));
        ___qtablewidgetitem2 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Placas", None));
        ___qtablewidgetitem3 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Hora entrada", None));
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Generar ticket", None))
        self.lineEdit_5.setText("")
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Placas Vehiculo", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Automovil", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Motocicleta", None))

        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Reivar Ticket", None))
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ticket", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Ticket:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Precio:", None))
        self.lineEdit_8.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ticket", None))
        self.lineEdit_9.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Precio", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Cobrar", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Pagar Ticket", None))
        self.lineEdit_10.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ticket", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Precio total horas + extravio:", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"TICKET:", None))
        self.lineEdit_24.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Placa del vehiculo", None))
        self.lineEdit_26.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Precio", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Revisar Placa", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"Cobrar", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Pagar Extravio Ticket", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Agregar Pensi\u00f3n", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Nombre: ", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Telefono:", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u" Correo:", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Tipo de Cliente:", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Tipo de Vehiculo:", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Placa:", None))
        self.lineEdit_29.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nombre completo", None))
        self.lineEdit_30.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Telefono", None))
        self.lineEdit_31.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Correo", None))
        self.lineEdit_32.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Placa del vehiculo", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"Cobrar y Dar Alta", None))
        self.comboBox_7.setItemText(0, QCoreApplication.translate("MainWindow", u"Automovil", None))
        self.comboBox_7.setItemText(1, QCoreApplication.translate("MainWindow", u"Motocicleta", None))

        self.comboBox_8.setItemText(0, QCoreApplication.translate("MainWindow", u"Pensionado", None))
        self.comboBox_8.setItemText(1, QCoreApplication.translate("MainWindow", u"Residente", None))

        self.comboBox_9.setItemText(0, QCoreApplication.translate("MainWindow", u"Dia", None))
        self.comboBox_9.setItemText(1, QCoreApplication.translate("MainWindow", u"Mes", None))

        self.label_58.setText(QCoreApplication.translate("MainWindow", u"Tipo de Pension:", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Precio", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Precio:", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Motivo por el cual se eliminara el ticket:", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"Borrar Ticket", None))
        self.lineEdit_33.setPlaceholderText(QCoreApplication.translate("MainWindow", u"TICKET ", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"Borrar Ticket", None))
        self.plainTextEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Motivo del borrado", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"Agregar Usuario ", None))
        self.lineEdit_34.setPlaceholderText(QCoreApplication.translate("MainWindow", u"nombre usuario", None))
        self.comboBox_10.setItemText(0, QCoreApplication.translate("MainWindow", u"Administrador", None))
        self.comboBox_10.setItemText(1, QCoreApplication.translate("MainWindow", u"Empleado", None))

        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a:", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Nombre completo:", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Usuario:", None))
        self.lineEdit_35.setPlaceholderText(QCoreApplication.translate("MainWindow", u"contrase\u00f1a", None))
        self.lineEdit_36.setPlaceholderText(QCoreApplication.translate("MainWindow", u"nombre completo", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u" Tipo de usuario:", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"Agregar Usuario", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"Modificar cuotas", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"Modificar Cuota", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"Precio Hora: ", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Tipo cliente: ", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Tipo de Vehiculo:", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Precio Extravio: ", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"Precio Dia: ", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"Precio Mes: ", None))
        self.comboBox_11.setItemText(0, QCoreApplication.translate("MainWindow", u"Automovil", None))
        self.comboBox_11.setItemText(1, QCoreApplication.translate("MainWindow", u"Motocicleta", None))

        self.comboBox_12.setItemText(0, QCoreApplication.translate("MainWindow", u"Normal", None))
        self.comboBox_12.setItemText(1, QCoreApplication.translate("MainWindow", u"Pensionado", None))
        self.comboBox_12.setItemText(2, QCoreApplication.translate("MainWindow", u"Residente", None))

        self.label_71.setText(QCoreApplication.translate("MainWindow", u"Realizar Reporte", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"Fecha Inicial", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"Fecha Final", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"Realizar Reporte", None))
        self.label_74.setText("")
    # retranslateUi

