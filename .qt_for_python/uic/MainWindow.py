# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1299, 913)
        MainWindow.setCursor(QCursor(Qt.ArrowCursor))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 1285, 911))
        self.label.setCursor(QCursor(Qt.BusyCursor))
        self.label.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(0, 0, 20, 255), stop:1 rgba(0, 255, 255, 255));\n"
"\n"
"")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(30, 730, 791, 101))
        self.groupBox.setStyleSheet(u"font: 75 14pt \"Comic Sans MS\";\n"
"color:rgb(250, 250, 250)")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(21, 41, 36, 26))
        self.comboBoxCOM = QComboBox(self.groupBox)
        self.comboBoxCOM.addItem("")
        self.comboBoxCOM.setObjectName(u"comboBoxCOM")
        self.comboBoxCOM.setGeometry(QRect(63, 43, 66, 24))
        self.comboBoxCOM.setStyleSheet(u" font: 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(0, 41, 58);")
        self.comboBoxCOM.setEditable(True)
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(251, 41, 83, 26))
        self.comboBoxBuadRate = QComboBox(self.groupBox)
        self.comboBoxBuadRate.addItem("")
        self.comboBoxBuadRate.addItem("")
        self.comboBoxBuadRate.addItem("")
        self.comboBoxBuadRate.setObjectName(u"comboBoxBuadRate")
        self.comboBoxBuadRate.setGeometry(QRect(340, 43, 80, 24))
        self.comboBoxBuadRate.setStyleSheet(u" font: 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(0, 41, 58);")
        self.comboBoxBuadRate.setEditable(True)
        self.btnConnect = QPushButton(self.groupBox)
        self.btnConnect.setObjectName(u"btnConnect")
        self.btnConnect.setGeometry(QRect(499, 33, 121, 41))
        self.btnConnect.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnConnect.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(0, 54, 69);\n"
"   border-radius: 10px;\n"
"border-color: rgb(255, 85, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Comic Sans MS\";\n"
"}\n"
"\n"
"QPushButton::hover\n"
"{\n"
"border:0px;\n"
"	\n"
"	background-color: rgb(0, 121, 131);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"border:1px solid rgb(0, 121, 131);\n"
"background-color: rgb(179,250, 250);\n"
"}")
        self.btndisconnect = QPushButton(self.groupBox)
        self.btndisconnect.setObjectName(u"btndisconnect")
        self.btndisconnect.setGeometry(QRect(650, 33, 121, 41))
        self.btndisconnect.setCursor(QCursor(Qt.PointingHandCursor))
        self.btndisconnect.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(0, 54, 69);\n"
"   border-radius: 10px;\n"
"border-color: rgb(255, 85, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Comic Sans MS\";\n"
"}\n"
"\n"
"QPushButton::hover\n"
"{\n"
"border:0px;\n"
"	\n"
"	background-color: rgb(0, 121, 131);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"border:1px solid rgb(0, 121, 131);\n"
"background-color: rgb(179,250, 250);\n"
"}")
        self.groupBox_5 = QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(20, 80, 1271, 441))
        self.groupBox_5.setBaseSize(QSize(0, 0))
        self.groupBox_5.setStyleSheet(u"font: 75 14pt \"Comic Sans MS\";\n"
"border-color: rgb(7, 7, 7);\n"
"color:rgb(250, 250, 250)")
        self.groupBox_5.setFlat(False)
        self.groupBox_5.setCheckable(False)
        self.groupBox_12 = QGroupBox(self.groupBox_5)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.groupBox_12.setGeometry(QRect(820, 60, 221, 361))
        self.groupBox_12.setStyleSheet(u"color: rgb(0, 110, 122);\n"
"font: 75 14pt \"Comic Sans MS\";")
        self.dialRPM = QDial(self.groupBox_12)
        self.dialRPM.setObjectName(u"dialRPM")
        self.dialRPM.setGeometry(QRect(10, 30, 201, 231))
        font = QFont()
        font.setFamily(u"Comic Sans MS")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.dialRPM.setFont(font)
        self.dialRPM.setCursor(QCursor(Qt.ClosedHandCursor))
        self.dialRPM.setStyleSheet(u" QDial\n"
"     {\n"
"      \n"
"	background-color: rgb(0, 0, 0);\n"
"        }\n"
"")
        self.dialRPM.setNotchesVisible(True)
        self.lineEditRPM = QLineEdit(self.groupBox_12)
        self.lineEditRPM.setObjectName(u"lineEditRPM")
        self.lineEditRPM.setGeometry(QRect(60, 270, 101, 29))
        self.lineEditRPM.setCursor(QCursor(Qt.IBeamCursor))
        self.lineEditRPM.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(193, 193, 193);\n"
"\n"
"                                        \n"
"	background-color: rgb(0, 54, 69);\n"
"                                        border: 2px solid gray;\n"
"                                        border-radius: 10px;\n"
"                                        padding: 0 8px;\n"
"                                       selection-background-color: darkgray;\n"
"                                        font-size: 16px;\n"
"}\n"
"\n"
"                                        QLineEdit:focus {\n"
"                                        \n"
"	background-color: rgb(179,250, 250);\n"
"                                       }\n"
"QLineEdit::hover\n"
"{\n"
"border:0px;\n"
"		background-color: rgb(179, 0, 0);\n"
"}")
        self.lineEditRPM.setEchoMode(QLineEdit.Normal)
        self.lineEditRPM.setAlignment(Qt.AlignCenter)
        self.groupBox_13 = QGroupBox(self.groupBox_5)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.groupBox_13.setGeometry(QRect(1050, 60, 221, 361))
        self.groupBox_13.setStyleSheet(u"color: rgb(0, 110, 122);\n"
"font: 75 14pt \"Comic Sans MS\";")
        self.lineEditSPEED = QLineEdit(self.groupBox_13)
        self.lineEditSPEED.setObjectName(u"lineEditSPEED")
        self.lineEditSPEED.setGeometry(QRect(60, 270, 101, 29))
        self.lineEditSPEED.setCursor(QCursor(Qt.IBeamCursor))
        self.lineEditSPEED.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(193, 193, 193);\n"
"\n"
"                                        \n"
"	background-color: rgb(0, 54, 69);\n"
"                                        border: 2px solid gray;\n"
"                                        border-radius: 10px;\n"
"                                        padding: 0 8px;\n"
"                                       selection-background-color: darkgray;\n"
"                                        font-size: 16px;\n"
"}\n"
"\n"
"                                        QLineEdit:focus {\n"
"                                        \n"
"	background-color: rgb(179,250, 250);\n"
"                                       }\n"
"QLineEdit::hover\n"
"{\n"
"border:0px;\n"
"		background-color: rgb(179, 0, 0);\n"
"}")
        self.lineEditSPEED.setEchoMode(QLineEdit.Normal)
        self.lineEditSPEED.setAlignment(Qt.AlignCenter)
        self.dialSPEED = QDial(self.groupBox_13)
        self.dialSPEED.setObjectName(u"dialSPEED")
        self.dialSPEED.setGeometry(QRect(10, 30, 201, 231))
        self.dialSPEED.setCursor(QCursor(Qt.ClosedHandCursor))
        self.dialSPEED.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.dialSPEED.setNotchesVisible(True)
        self.groupBox_26 = QGroupBox(self.groupBox_5)
        self.groupBox_26.setObjectName(u"groupBox_26")
        self.groupBox_26.setGeometry(QRect(580, 287, 160, 121))
        self.groupBox_26.setStyleSheet(u"color: rgb(0, 208, 211);\n"
"font: 75 14pt \"Comic Sans MS\";")
        self.verticalSliderRESERVE2 = QSlider(self.groupBox_26)
        self.verticalSliderRESERVE2.setObjectName(u"verticalSliderRESERVE2")
        self.verticalSliderRESERVE2.setGeometry(QRect(110, 20, 20, 81))
        self.verticalSliderRESERVE2.setCursor(QCursor(Qt.OpenHandCursor))
        self.verticalSliderRESERVE2.setMaximum(255)
        self.verticalSliderRESERVE2.setOrientation(Qt.Vertical)
        self.verticalSliderRESERVE2.setTickPosition(QSlider.TicksBelow)
        self.lineEditReserve2 = QLineEdit(self.groupBox_26)
        self.lineEditReserve2.setObjectName(u"lineEditReserve2")
        self.lineEditReserve2.setGeometry(QRect(30, 50, 71, 29))
        self.lineEditReserve2.setCursor(QCursor(Qt.IBeamCursor))
        self.lineEditReserve2.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(193, 193, 193);\n"
"\n"
"                                        \n"
"	background-color: rgb(0, 54, 69);\n"
"                                        border: 2px solid gray;\n"
"                                        border-radius: 10px;\n"
"                                        padding: 0 8px;\n"
"                                       selection-background-color: darkgray;\n"
"                                        font-size: 16px;\n"
"}\n"
"\n"
"                                        QLineEdit:focus {\n"
"                                        \n"
"	background-color: rgb(179,250, 250);\n"
"                                       }\n"
"QLineEdit::hover\n"
"{\n"
"border:0px;\n"
"		background-color: rgb(179, 0, 0);\n"
"}")
        self.lineEditReserve2.setEchoMode(QLineEdit.Normal)
        self.lineEditReserve2.setAlignment(Qt.AlignCenter)
        self.groupBox_16 = QGroupBox(self.groupBox_5)
        self.groupBox_16.setObjectName(u"groupBox_16")
        self.groupBox_16.setGeometry(QRect(580, 168, 160, 121))
        self.groupBox_16.setStyleSheet(u"color: rgb(0, 208, 211);\n"
"font: 75 14pt \"Comic Sans MS\";")
        self.verticalSliderRESERVE1 = QSlider(self.groupBox_16)
        self.verticalSliderRESERVE1.setObjectName(u"verticalSliderRESERVE1")
        self.verticalSliderRESERVE1.setGeometry(QRect(110, 20, 20, 81))
        self.verticalSliderRESERVE1.setCursor(QCursor(Qt.OpenHandCursor))
        self.verticalSliderRESERVE1.setMaximum(255)
        self.verticalSliderRESERVE1.setOrientation(Qt.Vertical)
        self.verticalSliderRESERVE1.setTickPosition(QSlider.TicksBelow)
        self.lineEditReserve1 = QLineEdit(self.groupBox_16)
        self.lineEditReserve1.setObjectName(u"lineEditReserve1")
        self.lineEditReserve1.setGeometry(QRect(30, 50, 71, 29))
        self.lineEditReserve1.setCursor(QCursor(Qt.IBeamCursor))
        self.lineEditReserve1.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(193, 193, 193);\n"
"\n"
"                                        \n"
"	background-color: rgb(0, 54, 69);\n"
"                                        border: 2px solid gray;\n"
"                                        border-radius: 10px;\n"
"                                        padding: 0 8px;\n"
"                                       selection-background-color: darkgray;\n"
"                                        font-size: 16px;\n"
"}\n"
"\n"
"                                        QLineEdit:focus {\n"
"                                        \n"
"	background-color: rgb(179,250, 250);\n"
"                                       }\n"
"QLineEdit::hover\n"
"{\n"
"border:0px;\n"
"		background-color: rgb(179, 0, 0);\n"
"}")
        self.lineEditReserve1.setEchoMode(QLineEdit.Normal)
        self.lineEditReserve1.setAlignment(Qt.AlignCenter)
        self.groupBox_17 = QGroupBox(self.groupBox_5)
        self.groupBox_17.setObjectName(u"groupBox_17")
        self.groupBox_17.setGeometry(QRect(580, 50, 160, 121))
        self.groupBox_17.setStyleSheet(u"color: rgb(0, 208, 211);\n"
"font: 75 14pt \"Comic Sans MS\";")
        self.verticalSliderDO2S = QSlider(self.groupBox_17)
        self.verticalSliderDO2S.setObjectName(u"verticalSliderDO2S")
        self.verticalSliderDO2S.setGeometry(QRect(110, 20, 20, 81))
        self.verticalSliderDO2S.setCursor(QCursor(Qt.OpenHandCursor))
        self.verticalSliderDO2S.setMaximum(255)
        self.verticalSliderDO2S.setOrientation(Qt.Vertical)
        self.verticalSliderDO2S.setTickPosition(QSlider.TicksBelow)
        self.lineEditDo2S = QLineEdit(self.groupBox_17)
        self.lineEditDo2S.setObjectName(u"lineEditDo2S")
        self.lineEditDo2S.setGeometry(QRect(30, 50, 71, 29))
        self.lineEditDo2S.setCursor(QCursor(Qt.IBeamCursor))
        self.lineEditDo2S.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(193, 193, 193);\n"
"\n"
"                                        \n"
"	background-color: rgb(0, 54, 69);\n"
"                                        border: 2px solid gray;\n"
"                                        border-radius: 10px;\n"
"                                        padding: 0 8px;\n"
"                                       selection-background-color: darkgray;\n"
"                                        font-size: 16px;\n"
"}\n"
"\n"
"                                        QLineEdit:focus {\n"
"                                        \n"
"	background-color: rgb(179,250, 250);\n"
"                                       }\n"
"QLineEdit::hover\n"
"{\n"
"border:0px;\n"
"		background-color: rgb(179, 0, 0);\n"
"}")
        self.lineEditDo2S.setEchoMode(QLineEdit.Normal)
        self.lineEditDo2S.setAlignment(Qt.AlignCenter)
        self.groupBox_2 = QGroupBox(self.groupBox_5)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(25, 50, 160, 121))
        self.groupBox_2.setStyleSheet(u"color: rgb(0, 208, 211);\n"
"font: 75 14pt \"Comic Sans MS\";")
        self.verticalSliderCTS = QSlider(self.groupBox_2)
        self.verticalSliderCTS.setObjectName(u"verticalSliderCTS")
        self.verticalSliderCTS.setGeometry(QRect(110, 20, 20, 81))
        self.verticalSliderCTS.setCursor(QCursor(Qt.OpenHandCursor))
        self.verticalSliderCTS.setStyleSheet(u"color: rgb(0, 247, 119);")
        self.verticalSliderCTS.setMaximum(255)
        self.verticalSliderCTS.setOrientation(Qt.Vertical)
        self.verticalSliderCTS.setTickPosition(QSlider.TicksBelow)
        self.lineEditCTS = QLineEdit(self.groupBox_2)
        self.lineEditCTS.setObjectName(u"lineEditCTS")
        self.lineEditCTS.setGeometry(QRect(30, 50, 71, 29))
        self.lineEditCTS.setCursor(QCursor(Qt.IBeamCursor))
        self.lineEditCTS.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(193, 193, 193);\n"
"\n"
"                                        \n"
"	background-color: rgb(0, 54, 69);\n"
"                                        border: 2px solid gray;\n"
"                                        border-radius: 10px;\n"
"                                        padding: 0 8px;\n"
"                                       selection-background-color: darkgray;\n"
"                                        font-size: 16px;\n"
"}\n"
"\n"
"                                        QLineEdit:focus {\n"
"                                        \n"
"	background-color: rgb(179,250, 250);\n"
"                                       }\n"
"QLineEdit::hover\n"
"{\n"
"border:0px;\n"
"		background-color: rgb(179, 0, 0);\n"
"}")
        self.lineEditCTS.setEchoMode(QLineEdit.Normal)
        self.lineEditCTS.setAlignment(Qt.AlignCenter)
        self.groupBox_8 = QGroupBox(self.groupBox_5)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setGeometry(QRect(395, 168, 160, 121))
        self.groupBox_8.setStyleSheet(u"color: rgb(0, 208, 211);\n"
"font: 75 14pt \"Comic Sans MS\";")
        self.verticalSliderPVS1 = QSlider(self.groupBox_8)
        self.verticalSliderPVS1.setObjectName(u"verticalSliderPVS1")
        self.verticalSliderPVS1.setGeometry(QRect(110, 20, 20, 81))
        self.verticalSliderPVS1.setCursor(QCursor(Qt.OpenHandCursor))
        self.verticalSliderPVS1.setMaximum(255)
        self.verticalSliderPVS1.setOrientation(Qt.Vertical)
        self.verticalSliderPVS1.setTickPosition(QSlider.TicksBelow)
        self.lineEditPVS1 = QLineEdit(self.groupBox_8)
        self.lineEditPVS1.setObjectName(u"lineEditPVS1")
        self.lineEditPVS1.setGeometry(QRect(30, 50, 71, 29))
        self.lineEditPVS1.setCursor(QCursor(Qt.IBeamCursor))
        self.lineEditPVS1.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(193, 193, 193);\n"
"\n"
"                                        \n"
"	background-color: rgb(0, 54, 69);\n"
"                                        border: 2px solid gray;\n"
"                                        border-radius: 10px;\n"
"                                        padding: 0 8px;\n"
"                                       selection-background-color: darkgray;\n"
"                                        font-size: 16px;\n"
"}\n"
"\n"
"                                        QLineEdit:focus {\n"
"                                        \n"
"	background-color: rgb(179,250, 250);\n"
"                                       }\n"
"QLineEdit::hover\n"
"{\n"
"border:0px;\n"
"		background-color: rgb(179, 0, 0);\n"
"}")
        self.lineEditPVS1.setEchoMode(QLineEdit.Normal)
        self.lineEditPVS1.setAlignment(Qt.AlignCenter)
        self.groupBox_6 = QGroupBox(self.groupBox_5)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(25, 168, 160, 121))
        self.groupBox_6.setStyleSheet(u"color: rgb(0, 208, 211);\n"
"font: 75 14pt \"Comic Sans MS\";")
        self.verticalSliderMAT = QSlider(self.groupBox_6)
        self.verticalSliderMAT.setObjectName(u"verticalSliderMAT")
        self.verticalSliderMAT.setGeometry(QRect(110, 20, 20, 81))
        self.verticalSliderMAT.setCursor(QCursor(Qt.OpenHandCursor))
        self.verticalSliderMAT.setMaximum(255)
        self.verticalSliderMAT.setOrientation(Qt.Vertical)
        self.verticalSliderMAT.setTickPosition(QSlider.TicksBelow)
        self.lineEditMAT = QLineEdit(self.groupBox_6)
        self.lineEditMAT.setObjectName(u"lineEditMAT")
        self.lineEditMAT.setGeometry(QRect(30, 50, 71, 29))
        self.lineEditMAT.setCursor(QCursor(Qt.IBeamCursor))
        self.lineEditMAT.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(193, 193, 193);\n"
"\n"
"                                        \n"
"	background-color: rgb(0, 54, 69);\n"
"                                        border: 2px solid gray;\n"
"                                        border-radius: 10px;\n"
"                                        padding: 0 8px;\n"
"                                       selection-background-color: darkgray;\n"
"                                        font-size: 16px;\n"
"}\n"
"\n"
"                                        QLineEdit:focus {\n"
"                                        \n"
"	background-color: rgb(179,250, 250);\n"
"                                       }\n"
"QLineEdit::hover\n"
"{\n"
"border:0px;\n"
"		background-color: rgb(179, 0, 0);\n"
"}")
        self.lineEditMAT.setEchoMode(QLineEdit.Normal)
        self.lineEditMAT.setAlignment(Qt.AlignCenter)
        self.groupBox_4 = QGroupBox(self.groupBox_5)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(395, 50, 160, 121))
        self.groupBox_4.setStyleSheet(u"color: rgb(0, 208, 211);\n"
"font: 75 14pt \"Comic Sans MS\";")
        self.verticalSliderTPS2 = QSlider(self.groupBox_4)
        self.verticalSliderTPS2.setObjectName(u"verticalSliderTPS2")
        self.verticalSliderTPS2.setGeometry(QRect(110, 20, 20, 81))
        self.verticalSliderTPS2.setCursor(QCursor(Qt.OpenHandCursor))
        self.verticalSliderTPS2.setMaximum(255)
        self.verticalSliderTPS2.setOrientation(Qt.Vertical)
        self.verticalSliderTPS2.setTickPosition(QSlider.TicksBelow)
        self.lineEditTPS2 = QLineEdit(self.groupBox_4)
        self.lineEditTPS2.setObjectName(u"lineEditTPS2")
        self.lineEditTPS2.setGeometry(QRect(30, 50, 71, 29))
        self.lineEditTPS2.setCursor(QCursor(Qt.IBeamCursor))
        self.lineEditTPS2.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(193, 193, 193);\n"
"\n"
"                                        \n"
"	background-color: rgb(0, 54, 69);\n"
"                                        border: 2px solid gray;\n"
"                                        border-radius: 10px;\n"
"                                        padding: 0 8px;\n"
"                                       selection-background-color: darkgray;\n"
"                                        font-size: 16px;\n"
"}\n"
"\n"
"                                        QLineEdit:focus {\n"
"                                        \n"
"	background-color: rgb(179,250, 250);\n"
"                                       }\n"
"QLineEdit::hover\n"
"{\n"
"border:0px;\n"
"		background-color: rgb(179, 0, 0);\n"
"}")
        self.lineEditTPS2.setEchoMode(QLineEdit.Normal)
        self.lineEditTPS2.setAlignment(Qt.AlignCenter)
        self.groupBox_3 = QGroupBox(self.groupBox_5)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(210, 50, 160, 121))
        self.groupBox_3.setStyleSheet(u"color: rgb(0, 208, 211);\n"
"font: 75 14pt \"Comic Sans MS\";")
        self.verticalSliderTPS1 = QSlider(self.groupBox_3)
        self.verticalSliderTPS1.setObjectName(u"verticalSliderTPS1")
        self.verticalSliderTPS1.setGeometry(QRect(110, 20, 20, 81))
        self.verticalSliderTPS1.setCursor(QCursor(Qt.OpenHandCursor))
        self.verticalSliderTPS1.setMaximum(255)
        self.verticalSliderTPS1.setOrientation(Qt.Vertical)
        self.verticalSliderTPS1.setTickPosition(QSlider.TicksBelow)
        self.lineEditTPS1 = QLineEdit(self.groupBox_3)
        self.lineEditTPS1.setObjectName(u"lineEditTPS1")
        self.lineEditTPS1.setGeometry(QRect(30, 50, 71, 29))
        self.lineEditTPS1.setCursor(QCursor(Qt.IBeamCursor))
        self.lineEditTPS1.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(193, 193, 193);\n"
"\n"
"                                        \n"
"	background-color: rgb(0, 54, 69);\n"
"                                        border: 2px solid gray;\n"
"                                        border-radius: 10px;\n"
"                                        padding: 0 8px;\n"
"                                       selection-background-color: darkgray;\n"
"                                        font-size: 16px;\n"
"}\n"
"\n"
"                                        QLineEdit:focus {\n"
"                                        \n"
"	background-color: rgb(179,250, 250);\n"
"                                       }\n"
"QLineEdit::hover\n"
"{\n"
"border:0px;\n"
"		background-color: rgb(179, 0, 0);\n"
"}")
        self.lineEditTPS1.setEchoMode(QLineEdit.Normal)
        self.lineEditTPS1.setAlignment(Qt.AlignCenter)
        self.groupBox_9 = QGroupBox(self.groupBox_5)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setGeometry(QRect(210, 168, 160, 121))
        self.groupBox_9.setStyleSheet(u"color: rgb(0, 208, 211);\n"
"font: 75 14pt \"Comic Sans MS\";")
        self.verticalSliderFUELLEVEL = QSlider(self.groupBox_9)
        self.verticalSliderFUELLEVEL.setObjectName(u"verticalSliderFUELLEVEL")
        self.verticalSliderFUELLEVEL.setGeometry(QRect(110, 20, 20, 81))
        self.verticalSliderFUELLEVEL.setCursor(QCursor(Qt.OpenHandCursor))
        self.verticalSliderFUELLEVEL.setMaximum(255)
        self.verticalSliderFUELLEVEL.setOrientation(Qt.Vertical)
        self.verticalSliderFUELLEVEL.setTickPosition(QSlider.TicksBelow)
        self.lineEditFuelLevel = QLineEdit(self.groupBox_9)
        self.lineEditFuelLevel.setObjectName(u"lineEditFuelLevel")
        self.lineEditFuelLevel.setGeometry(QRect(30, 50, 71, 29))
        self.lineEditFuelLevel.setCursor(QCursor(Qt.IBeamCursor))
        self.lineEditFuelLevel.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(193, 193, 193);\n"
"\n"
"                                        \n"
"	background-color: rgb(0, 54, 69);\n"
"                                        border: 2px solid gray;\n"
"                                        border-radius: 10px;\n"
"                                        padding: 0 8px;\n"
"                                       selection-background-color: darkgray;\n"
"                                        font-size: 16px;\n"
"}\n"
"\n"
"                                        QLineEdit:focus {\n"
"                                        \n"
"	background-color: rgb(179,250, 250);\n"
"                                       }\n"
"QLineEdit::hover\n"
"{\n"
"border:0px;\n"
"		background-color: rgb(179, 0, 0);\n"
"}")
        self.lineEditFuelLevel.setEchoMode(QLineEdit.Normal)
        self.lineEditFuelLevel.setAlignment(Qt.AlignCenter)
        self.groupBox_10 = QGroupBox(self.groupBox_5)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.groupBox_10.setGeometry(QRect(210, 287, 160, 121))
        self.groupBox_10.setStyleSheet(u"color: rgb(0, 208, 211);\n"
"font: 75 14pt \"Comic Sans MS\";")
        self.verticalSliderMAP = QSlider(self.groupBox_10)
        self.verticalSliderMAP.setObjectName(u"verticalSliderMAP")
        self.verticalSliderMAP.setGeometry(QRect(110, 20, 20, 81))
        self.verticalSliderMAP.setCursor(QCursor(Qt.OpenHandCursor))
        self.verticalSliderMAP.setMaximum(255)
        self.verticalSliderMAP.setOrientation(Qt.Vertical)
        self.verticalSliderMAP.setTickPosition(QSlider.TicksBelow)
        self.lineEditMAP = QLineEdit(self.groupBox_10)
        self.lineEditMAP.setObjectName(u"lineEditMAP")
        self.lineEditMAP.setGeometry(QRect(30, 50, 71, 29))
        self.lineEditMAP.setCursor(QCursor(Qt.IBeamCursor))
        self.lineEditMAP.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(193, 193, 193);\n"
"\n"
"                                        \n"
"	background-color: rgb(0, 54, 69);\n"
"                                        border: 2px solid gray;\n"
"                                        border-radius: 10px;\n"
"                                        padding: 0 8px;\n"
"                                       selection-background-color: darkgray;\n"
"                                        font-size: 16px;\n"
"}\n"
"\n"
"                                        QLineEdit:focus {\n"
"                                        \n"
"	background-color: rgb(179,250, 250);\n"
"                                       }\n"
"QLineEdit::hover\n"
"{\n"
"border:0px;\n"
"		background-color: rgb(179, 0, 0);\n"
"}")
        self.lineEditMAP.setEchoMode(QLineEdit.Normal)
        self.lineEditMAP.setAlignment(Qt.AlignCenter)
        self.groupBox_11 = QGroupBox(self.groupBox_5)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.groupBox_11.setGeometry(QRect(25, 287, 160, 121))
        self.groupBox_11.setStyleSheet(u"color: rgb(0, 208, 211);\n"
"font: 75 14pt \"Comic Sans MS\";")
        self.verticalSliderPVS2 = QSlider(self.groupBox_11)
        self.verticalSliderPVS2.setObjectName(u"verticalSliderPVS2")
        self.verticalSliderPVS2.setGeometry(QRect(110, 20, 20, 81))
        self.verticalSliderPVS2.setCursor(QCursor(Qt.OpenHandCursor))
        self.verticalSliderPVS2.setMaximum(255)
        self.verticalSliderPVS2.setOrientation(Qt.Vertical)
        self.verticalSliderPVS2.setTickPosition(QSlider.TicksBelow)
        self.lineEditPVS2 = QLineEdit(self.groupBox_11)
        self.lineEditPVS2.setObjectName(u"lineEditPVS2")
        self.lineEditPVS2.setGeometry(QRect(30, 50, 71, 29))
        self.lineEditPVS2.setCursor(QCursor(Qt.IBeamCursor))
        self.lineEditPVS2.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(193, 193, 193);\n"
"\n"
"                                        \n"
"	background-color: rgb(0, 54, 69);\n"
"                                        border: 2px solid gray;\n"
"                                        border-radius: 10px;\n"
"                                        padding: 0 8px;\n"
"                                       selection-background-color: darkgray;\n"
"                                        font-size: 16px;\n"
"}\n"
"\n"
"                                        QLineEdit:focus {\n"
"                                        \n"
"	background-color: rgb(179,250, 250);\n"
"                                       }\n"
"QLineEdit::hover\n"
"{\n"
"border:0px;\n"
"		background-color: rgb(179, 0, 0);\n"
"}")
        self.lineEditPVS2.setEchoMode(QLineEdit.Normal)
        self.lineEditPVS2.setAlignment(Qt.AlignCenter)
        self.groupBox_22 = QGroupBox(self.groupBox_5)
        self.groupBox_22.setObjectName(u"groupBox_22")
        self.groupBox_22.setGeometry(QRect(395, 287, 160, 121))
        self.groupBox_22.setStyleSheet(u"color: rgb(0, 208, 211);\n"
"font: 75 14pt \"Comic Sans MS\";")
        self.verticalSliderUO2S = QSlider(self.groupBox_22)
        self.verticalSliderUO2S.setObjectName(u"verticalSliderUO2S")
        self.verticalSliderUO2S.setGeometry(QRect(110, 20, 20, 81))
        self.verticalSliderUO2S.setCursor(QCursor(Qt.OpenHandCursor))
        self.verticalSliderUO2S.setMaximum(255)
        self.verticalSliderUO2S.setOrientation(Qt.Vertical)
        self.verticalSliderUO2S.setTickPosition(QSlider.TicksBelow)
        self.lineEditUo2S = QLineEdit(self.groupBox_22)
        self.lineEditUo2S.setObjectName(u"lineEditUo2S")
        self.lineEditUo2S.setGeometry(QRect(30, 50, 71, 29))
        self.lineEditUo2S.setCursor(QCursor(Qt.IBeamCursor))
        self.lineEditUo2S.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(193, 193, 193);\n"
"\n"
"                                        \n"
"	background-color: rgb(0, 54, 69);\n"
"                                        border: 2px solid gray;\n"
"                                        border-radius: 10px;\n"
"                                        padding: 0 8px;\n"
"                                       selection-background-color: darkgray;\n"
"                                        font-size: 16px;\n"
"}\n"
"\n"
"                                        QLineEdit:focus {\n"
"                                        \n"
"	background-color: rgb(179,250, 250);\n"
"                                       }\n"
"QLineEdit::hover\n"
"{\n"
"border:0px;\n"
"		background-color: rgb(179, 0, 0);\n"
"}")
        self.lineEditUo2S.setEchoMode(QLineEdit.Normal)
        self.lineEditUo2S.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(420, 20, 341, 61))
        self.label_4.setStyleSheet(u"font: 75 28pt \"Comic Sans MS\";\n"
"color: rgb(255, 255, 255);")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(780, 780, 341, 61))
        self.label_5.setStyleSheet(u"font: 75 italic 20pt \"Comic Sans MS\";\n"
"color: rgb(255, 255, 255);")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.groupBox_14 = QGroupBox(self.centralwidget)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.groupBox_14.setGeometry(QRect(871, 531, 419, 199))
        self.groupBox_14.setCursor(QCursor(Qt.PointingHandCursor))
        self.groupBox_14.setStyleSheet(u"font: 75 14pt \"Comic Sans MS\";\n"
"color:rgb(250, 250, 250)")
        self.btnBattery = QPushButton(self.groupBox_14)
        self.btnBattery.setObjectName(u"btnBattery")
        self.btnBattery.setGeometry(QRect(100, 50, 105, 33))
        self.btnBattery.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnBattery.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(0, 54, 69);\n"
"   border-radius: 10px;\n"
"border-color: rgb(255, 85, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Comic Sans MS\";\n"
"}\n"
"\n"
"QPushButton::hover\n"
"{\n"
"border:0px;\n"
"	\n"
"	background-color: rgb(0, 121, 131);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"border:1px solid rgb(0, 121, 131);\n"
"background-color: rgb(179,250, 250);\n"
"}")
        self.btnSwitch = QPushButton(self.groupBox_14)
        self.btnSwitch.setObjectName(u"btnSwitch")
        self.btnSwitch.setGeometry(QRect(220, 50, 105, 33))
        self.btnSwitch.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnSwitch.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(0, 54, 69);\n"
"   border-radius: 10px;\n"
"border-color: rgb(255, 85, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Comic Sans MS\";\n"
"}\n"
"\n"
"QPushButton::hover\n"
"{\n"
"border:0px;\n"
"	\n"
"	background-color: rgb(0, 121, 131);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"border:1px solid rgb(0, 121, 131);\n"
"background-color: rgb(179,250, 250);\n"
"}")
        self.btnSendData = QPushButton(self.groupBox_14)
        self.btnSendData.setObjectName(u"btnSendData")
        self.btnSendData.setGeometry(QRect(100, 90, 231, 91))
        self.btnSendData.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnSendData.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(0, 54, 69);\n"
"   border-radius: 10px;\n"
"border-color: rgb(255, 85, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Comic Sans MS\";\n"
"}\n"
"\n"
"QPushButton::hover\n"
"{\n"
"border:0px;\n"
"	\n"
"	background-color: rgb(0, 121, 131);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"border:1px solid rgb(0, 121, 131);\n"
"	background-color: rgb(179,250, 250);\n"
"}")
        self.btnSendData.setAutoDefault(False)
        self.btnSendData.setFlat(False)
        self.groupBox_7 = QGroupBox(self.centralwidget)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setGeometry(QRect(21, 531, 419, 199))
        self.groupBox_7.setCursor(QCursor(Qt.ForbiddenCursor))
        self.groupBox_7.setStyleSheet(u"font: 75 14pt \"Comic Sans MS\";\n"
"color:rgb(250, 250, 250)")
        self.btnFANHIGH = QPushButton(self.groupBox_7)
        self.btnFANHIGH.setObjectName(u"btnFANHIGH")
        self.btnFANHIGH.setGeometry(QRect(30, 30, 105, 33))
        self.btnFANHIGH.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnFANHIGH.setStyleSheet(u"QPushButton {\n"
"                                        border-radius: 10px;\n"
"                                       selection-background-color: darkgray;\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"Comic Sans MS\";\n"
"\n"
"	background-color: rgb(250, 250, 250);\n"
"\n"
"border-color: rgb(255, 85, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton::hover\n"
"{\n"
"border:0px;\n"
"	\n"
"	background-color: rgb(0, 134, 144);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"border:1px solid rgb(0, 121, 131);\n"
"background-color: rgb(179,250, 250);\n"
"}")
        self.checkBoxFanHigh = QCheckBox(self.groupBox_7)
        self.checkBoxFanHigh.setObjectName(u"checkBoxFanHigh")
        self.checkBoxFanHigh.setGeometry(QRect(150, 30, 104, 28))
        self.checkBoxFanLow = QCheckBox(self.groupBox_7)
        self.checkBoxFanLow.setObjectName(u"checkBoxFanLow")
        self.checkBoxFanLow.setGeometry(QRect(150, 70, 104, 28))
        self.btnFANLOW = QPushButton(self.groupBox_7)
        self.btnFANLOW.setObjectName(u"btnFANLOW")
        self.btnFANLOW.setGeometry(QRect(30, 70, 105, 33))
        self.btnFANLOW.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnFANLOW.setStyleSheet(u"QPushButton {\n"
"                                        border-radius: 10px;\n"
"                                       selection-background-color: darkgray;\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"Comic Sans MS\";\n"
"\n"
"	background-color: rgb(250, 250, 250);\n"
"\n"
"border-color: rgb(255, 85, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton::hover\n"
"{\n"
"border:0px;\n"
"	\n"
"	background-color: rgb(0, 134, 144);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"border:1px solid rgb(0, 121, 131);\n"
"background-color: rgb(179,250, 250);\n"
"}")
        self.checkBoxAC = QCheckBox(self.groupBox_7)
        self.checkBoxAC.setObjectName(u"checkBoxAC")
        self.checkBoxAC.setGeometry(QRect(150, 110, 104, 28))
        self.btnAC = QPushButton(self.groupBox_7)
        self.btnAC.setObjectName(u"btnAC")
        self.btnAC.setGeometry(QRect(30, 110, 105, 33))
        self.btnAC.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnAC.setStyleSheet(u"QPushButton {\n"
"                                        border-radius: 10px;\n"
"                                       selection-background-color: darkgray;\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"Comic Sans MS\";\n"
"\n"
"	background-color: rgb(250, 250, 250);\n"
"\n"
"border-color: rgb(255, 85, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton::hover\n"
"{\n"
"border:0px;\n"
"	\n"
"	background-color: rgb(0, 134, 144);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"border:1px solid rgb(0, 121, 131);\n"
"background-color: rgb(179,250, 250);\n"
"}")
        self.checkBoxFuelPump = QCheckBox(self.groupBox_7)
        self.checkBoxFuelPump.setObjectName(u"checkBoxFuelPump")
        self.checkBoxFuelPump.setGeometry(QRect(150, 150, 104, 28))
        self.btnFUELPUMP = QPushButton(self.groupBox_7)
        self.btnFUELPUMP.setObjectName(u"btnFUELPUMP")
        self.btnFUELPUMP.setGeometry(QRect(30, 150, 105, 33))
        self.btnFUELPUMP.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnFUELPUMP.setStyleSheet(u"QPushButton {\n"
"                                        border-radius: 10px;\n"
"                                       selection-background-color: darkgray;\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"Comic Sans MS\";\n"
"\n"
"	background-color: rgb(250, 250, 250);\n"
"\n"
"border-color: rgb(255, 85, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton::hover\n"
"{\n"
"border:0px;\n"
"	\n"
"	background-color: rgb(0, 134, 144);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"border:1px solid rgb(0, 121, 131);\n"
"background-color: rgb(179,250, 250);\n"
"}")
        self.groupBox_15 = QGroupBox(self.centralwidget)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.groupBox_15.setGeometry(QRect(446, 531, 419, 199))
        self.groupBox_15.setStyleSheet(u"font: 75 14pt \"Comic Sans MS\";\n"
"color:rgb(250, 250, 250)")
        self.btnBrakeTest = QPushButton(self.groupBox_15)
        self.btnBrakeTest.setObjectName(u"btnBrakeTest")
        self.btnBrakeTest.setGeometry(QRect(80, 130, 111, 33))
        self.btnBrakeTest.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnBrakeTest.setStyleSheet(u"QPushButton {\n"
"                                        border-radius: 10px;\n"
"                                       selection-background-color: darkgray;\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"Comic Sans MS\";\n"
"\n"
"	background-color: rgb(250, 250, 250);\n"
"\n"
"border-color: rgb(255, 85, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton::hover\n"
"{\n"
"border:0px;\n"
"	\n"
"	background-color: rgb(0, 134, 144);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"border:1px solid rgb(0, 121, 131);\n"
"background-color: rgb(179,250, 250);\n"
"}")
        self.btnACSwitch2 = QPushButton(self.groupBox_15)
        self.btnACSwitch2.setObjectName(u"btnACSwitch2")
        self.btnACSwitch2.setGeometry(QRect(246, 80, 105, 33))
        self.btnACSwitch2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnACSwitch2.setStyleSheet(u"QPushButton {\n"
"                                        border-radius: 10px;\n"
"                                       selection-background-color: darkgray;\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"Comic Sans MS\";\n"
"\n"
"	background-color: rgb(250, 250, 250);\n"
"\n"
"border-color: rgb(255, 85, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton::hover\n"
"{\n"
"border:0px;\n"
"	\n"
"	background-color: rgb(0, 134, 144);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"border:1px solid rgb(0, 121, 131);\n"
"background-color: rgb(179,250, 250);\n"
"}")
        self.btnACSwitch1 = QPushButton(self.groupBox_15)
        self.btnACSwitch1.setObjectName(u"btnACSwitch1")
        self.btnACSwitch1.setGeometry(QRect(136, 80, 105, 33))
        self.btnACSwitch1.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnACSwitch1.setStyleSheet(u"QPushButton {\n"
"                                        border-radius: 10px;\n"
"                                       selection-background-color: darkgray;\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"Comic Sans MS\";\n"
"\n"
"	background-color: rgb(250, 250, 250);\n"
"\n"
"border-color: rgb(255, 85, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton::hover\n"
"{\n"
"border:0px;\n"
"	\n"
"	background-color: rgb(0, 134, 144);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"border:1px solid rgb(0, 121, 131);\n"
"background-color: rgb(179,250, 250);\n"
"}")
        self.btnPSV = QPushButton(self.groupBox_15)
        self.btnPSV.setObjectName(u"btnPSV")
        self.btnPSV.setGeometry(QRect(206, 130, 105, 33))
        self.btnPSV.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnPSV.setStyleSheet(u"QPushButton {\n"
"                                        border-radius: 10px;\n"
"                                       selection-background-color: darkgray;\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"Comic Sans MS\";\n"
"\n"
"	background-color: rgb(250, 250, 250);\n"
"\n"
"border-color: rgb(255, 85, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton::hover\n"
"{\n"
"border:0px;\n"
"	\n"
"	background-color: rgb(0, 134, 144);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"border:1px solid rgb(0, 121, 131);\n"
"background-color: rgb(179,250, 250);\n"
"}")
        self.btnCluch = QPushButton(self.groupBox_15)
        self.btnCluch.setObjectName(u"btnCluch")
        self.btnCluch.setGeometry(QRect(26, 80, 105, 33))
        self.btnCluch.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnCluch.setStyleSheet(u"QPushButton {\n"
"                                        border-radius: 10px;\n"
"                                       selection-background-color: darkgray;\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"Comic Sans MS\";\n"
"\n"
"	background-color: rgb(250, 250, 250);\n"
"\n"
"border-color: rgb(255, 85, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton::hover\n"
"{\n"
"border:0px;\n"
"	\n"
"	background-color: rgb(0, 134, 144);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"border:1px solid rgb(0, 121, 131);\n"
"background-color: rgb(179,250, 250);\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)
        self.label.raise_()
        self.groupBox_14.raise_()
        self.groupBox_7.raise_()
        self.groupBox_15.raise_()
        self.groupBox_5.raise_()
        self.groupBox.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1299, 19))
        font1 = QFont()
        font1.setFamily(u"MS Shell Dlg 2")
        font1.setPointSize(9)
        self.menubar.setFont(font1)
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuSetting = QMenu(self.menubar)
        self.menuSetting.setObjectName(u"menuSetting")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuSetting.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)

        self.btnSendData.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"TesterECU", None))
        self.label.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Connection", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Com", None))
        self.comboBoxCOM.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"BuadRate", None))
        self.comboBoxBuadRate.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.comboBoxBuadRate.setItemText(1, QCoreApplication.translate("MainWindow", u"9600", None))
        self.comboBoxBuadRate.setItemText(2, QCoreApplication.translate("MainWindow", u"115200", None))

        self.btnConnect.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.btndisconnect.setText(QCoreApplication.translate("MainWindow", u"Disconnect", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Analog Data", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("MainWindow", u"RPM", None))
        self.lineEditRPM.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.groupBox_13.setTitle(QCoreApplication.translate("MainWindow", u"Speed", None))
        self.lineEditSPEED.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.groupBox_26.setTitle(QCoreApplication.translate("MainWindow", u"Reserved2", None))
        self.verticalSliderRESERVE2.setStyleSheet(QCoreApplication.translate("MainWindow", u"color: rgb(0, 247, 119);", None))
        self.lineEditReserve2.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.groupBox_16.setTitle(QCoreApplication.translate("MainWindow", u"Reserved1", None))
        self.verticalSliderRESERVE1.setStyleSheet(QCoreApplication.translate("MainWindow", u"color: rgb(0, 247, 119);", None))
        self.lineEditReserve1.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.groupBox_17.setTitle(QCoreApplication.translate("MainWindow", u"Do2s", None))
        self.verticalSliderDO2S.setStyleSheet(QCoreApplication.translate("MainWindow", u"color: rgb(0, 247, 119);", None))
        self.lineEditDo2S.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"CTS", None))
        self.lineEditCTS.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"PVS1", None))
        self.verticalSliderPVS1.setStyleSheet(QCoreApplication.translate("MainWindow", u"color: rgb(0, 247, 119);", None))
        self.lineEditPVS1.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"MAT", None))
        self.verticalSliderMAT.setStyleSheet(QCoreApplication.translate("MainWindow", u"color: rgb(0, 247, 119);", None))
        self.lineEditMAT.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"TPS2", None))
        self.verticalSliderTPS2.setStyleSheet(QCoreApplication.translate("MainWindow", u"color: rgb(0, 247, 119);", None))
        self.lineEditTPS2.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"TPS1", None))
        self.verticalSliderTPS1.setStyleSheet(QCoreApplication.translate("MainWindow", u"color: rgb(0, 247, 119);", None))
        self.lineEditTPS1.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"FuelLevel", None))
        self.verticalSliderFUELLEVEL.setStyleSheet(QCoreApplication.translate("MainWindow", u"color: rgb(0, 247, 119);", None))
        self.lineEditFuelLevel.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"MAP", None))
        self.verticalSliderMAP.setStyleSheet(QCoreApplication.translate("MainWindow", u"color: rgb(0, 247, 119);", None))
        self.lineEditMAP.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"PVS2", None))
        self.verticalSliderPVS2.setStyleSheet(QCoreApplication.translate("MainWindow", u"color: rgb(0, 247, 119);", None))
        self.lineEditPVS2.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.groupBox_22.setTitle(QCoreApplication.translate("MainWindow", u"Uo2s", None))
        self.verticalSliderUO2S.setStyleSheet(QCoreApplication.translate("MainWindow", u"color: rgb(0, 247, 119);", None))
        self.lineEditUo2S.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"ECU Tester AZMT", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Azin Electro Idea", None))
        self.groupBox_14.setTitle(QCoreApplication.translate("MainWindow", u"Power", None))
        self.btnBattery.setText(QCoreApplication.translate("MainWindow", u"Battery", None))
        self.btnSwitch.setText(QCoreApplication.translate("MainWindow", u"Switch", None))
        self.btnSendData.setText(QCoreApplication.translate("MainWindow", u"Send Data", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"ActuatorData", None))
        self.btnFANHIGH.setText(QCoreApplication.translate("MainWindow", u"FanHigh", None))
        self.checkBoxFanHigh.setText("")
        self.checkBoxFanLow.setText("")
        self.btnFANLOW.setText(QCoreApplication.translate("MainWindow", u"FanLow", None))
        self.checkBoxAC.setText("")
        self.btnAC.setText(QCoreApplication.translate("MainWindow", u"AC Compressor", None))
        self.checkBoxFuelPump.setText("")
        self.btnFUELPUMP.setText(QCoreApplication.translate("MainWindow", u"FuelPump", None))
        self.groupBox_15.setTitle(QCoreApplication.translate("MainWindow", u"Digital Data", None))
        self.btnBrakeTest.setText(QCoreApplication.translate("MainWindow", u"BrakeTestSwitch", None))
        self.btnACSwitch2.setText(QCoreApplication.translate("MainWindow", u"AC SWITCH 2", None))
        self.btnACSwitch1.setText(QCoreApplication.translate("MainWindow", u"AC SWITCH 1", None))
        self.btnPSV.setText(QCoreApplication.translate("MainWindow", u"PSV", None))
        self.btnCluch.setText(QCoreApplication.translate("MainWindow", u"Clutch", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuSetting.setTitle(QCoreApplication.translate("MainWindow", u"Setting", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

