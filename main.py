import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2 import QtWidgets
from PySide2.QtCore import QFile

from PySide2 import QtCore, QtWidgets, QtSerialPort
import serial
import serial.tools.list_ports
import os
os.system("pyside2-uic Mainwindow.ui -o mainwindow.py")
from mainwindow import Ui_MainWindow



class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
   def __init__(self):
      super(MainWindow, self).__init__()
      self.setupUi(self)
      self.Message = bytearray(32) #defining a variable with 32 bytes of data, if u want to change bits u need to use shift and | and & operators
      self.Message[0] = 0xFF
      self.lineEditCTS.returnPressed.connect(lambda:self.text_changed("CTS0"))#event active with enter key
      self.lineEditDo2S.returnPressed.connect(lambda:self.text_changed("Do2S0"))
      self.lineEditFuelLevel.returnPressed.connect(lambda:self.text_changed("FuelLevel0"))
      self.lineEditMAP.returnPressed.connect(lambda:self.text_changed("MAP0"))
      self.lineEditMAT.returnPressed.connect(lambda:self.text_changed("MAT0"))
      self.lineEditPVS1.returnPressed.connect(lambda:self.text_changed("PVS10"))
      self.lineEditPVS2.returnPressed.connect(lambda:self.text_changed("PVS20"))
      self.lineEditRPM.returnPressed.connect(lambda:self.text_changed("RPM0"))
      self.lineEditSPEED.returnPressed.connect(lambda:self.text_changed("SPEED0"))
      self.lineEditTPS1.returnPressed.connect(lambda:self.text_changed("TPS10"))
      self.lineEditTPS2.returnPressed.connect(lambda:self.text_changed("TPS20"))
      self.lineEditUo2S.returnPressed.connect(lambda:self.text_changed("Uo2S0"))
      self.lineEditReserve1.returnPressed.connect(lambda:self.text_changed("Reserve10"))
      self.lineEditReserve2.returnPressed.connect(lambda:self.text_changed("Reserve20"))


      self.verticalSliderCTS.valueChanged.connect(lambda:self.text_changed("CTS1"))
      self.verticalSliderDO2S.valueChanged.connect(lambda:self.text_changed("Do2S1"))
      self.verticalSliderFUELLEVEL.valueChanged.connect(lambda:self.text_changed("FUELLEVEL1"))
      self.verticalSliderMAP.valueChanged.connect(lambda:self.text_changed("MAP0"))
      self.verticalSliderMAP.valueChanged.connect(lambda:self.text_changed("MAT0"))
      self.verticalSliderPVS1.valueChanged.connect(lambda:self.text_changed("PVS10"))
      self.verticalSliderPVS2.valueChanged.connect(lambda:self.text_changed("PVS20"))
      self.verticalSliderTPS1.valueChanged.connect(lambda:self.text_changed("TPS10"))
      self.verticalSliderTPS2.valueChanged.connect(lambda:self.text_changed("TPS20"))
      self.verticalSliderUO2S.valueChanged.connect(lambda:self.text_changed("Uo2S0"))
      self.verticalSliderRESERVE1.valueChanged.connect(lambda:self.text_changed("Reserve10"))
      self.verticalSliderRESERVE2.valueChanged.connect(lambda:self.text_changed("Reserve20"))





      # self.Message[1] = self.CreateByte(1, 0, 1, 0, 1, 0, 0, 1)#set 8 bits in one byte
      #self.DisEnable(False)
      self.btnConnect.clicked.connect(self.ConnectSerial)
      self.btndisconnect.clicked.connect(self.DisconnectSerial)
      # self.lineEdit.setInputMask("0x-HH");
      #self.btnSend.clicked.connect(lambda : self.ser.write(self.Message)) u can use this instead of defining function
      self.btnSendData.clicked.connect(self.SendSerial)
      Ports = serial.tools.list_ports.comports() # make a list from available COM ports. u should print this to see whole list
      for this in Ports:
          #com = str(this)
          #self.comboBox.addItem(com[com.find('COM'):com.find('COM')+5])
          self.comboBoxCOM.addItem(str(this))


   def ConnectSerial(self):
      com = self.comboBoxCOM.currentText()
      com = com[com.find('COM'):com.find('COM')+4]#select only COM# from whole text, u need to put com# in next line
      self.ser = serial.Serial(
         port = com,#u can pu any com u want here for example "COM4" or "COM3". it need to be string
         baudrate = 115200,
         parity = serial.PARITY_NONE,
         stopbits = serial.STOPBITS_ONE,
         bytesize = serial.EIGHTBITS,
         timeout = 100)
      if self.ser.isOpen():# returns true if port was open
         self.DisEnable(True)

   def text_changed(self,event):
      if event=="CTS0":
         self.verticalSliderCTS.setValue(int(self.lineEditCTS.text()))
         CTSValue0=self.lineEditCTS.text()
         print(CTSValue0)

      if event=="CTS1":
         self.lineEditCTS.setText(str(self.verticalSliderCTS.value()))
         CTSValue1=self.verticalSliderCTS.value()
         print(CTSValue1)

      if event=="Do2S0":
         self.verticalSliderDO2S.setValue(int(self.lineEditDo2S.text()))
         Do2S0=self.lineEditDo2S.text()
         print(Do2S0)

      if event=="Do2S1":
         self.lineEditDo2S.setText(str(self.verticalSliderDO2S.value()))
         Do2S1=self.verticalSliderDO2S.value()
         print(Do2S1)


      if event=="FuelLevel0":
         self.verticalSliderFUELLEVEL.setValue(int(self.lineEditFuelLevel.text()))
         FuelLevel0Value0=self.lineEditFuelLevel.text()
         print(FuelLevel0Value0)

      if event=="FuelLevel1":
         self.lineEditCTS.setText(str(self.verticalSliderCTS.value()))
         FuelLevel1Value1=self.verticalSliderFUELLEVEL.value()
         print(FuelLevel1Value1)

      if event=="MAP0":
         self.verticalSliderCTS.setValue(int(self.lineEditCTS.text()))
         CTSValue0=self.lineEditCTS.text()
         print(CTSValue0)

      if event=="MAP1":
         CTSValue1=self.lineEditCTS.setText(str(self.verticalSliderCTS.value()))
         print(CTSValue1)

      if event=="PVS10":
         self.verticalSliderPVS1.setValue(int(self.lineEditPVS1.text()))
         PVS10Value0=self.lineEditPVS1.text()
         print(PVS10Value0)

      # if event=="PVS11":
      #    CTSValue1=self.lineEditCTS.setText(str(self.verticalSliderCTS.value()))
      #    print(CTSValue1)

      if event=="PVS20":
         self.verticalSliderPVS2.setValue(int(self.lineEditPVS2.text()))
         PVS20Value0=self.lineEditPVS2.text()
         print(PVS20Value0)

      # if event=="PVS21":
      #    CTSValue1=self.lineEditCTS.setText(str(self.verticalSliderCTS.value()))
      #    print(CTSValue1)
   
      if event=="RPM0":
         RPM0Value0=self.lineEditRPM.text()
         print(RPM0Value0)

      if event=="SPEED0":
         SPEED0=self.lineEditSPEED.text()
         print(SPEED0)

      if event=="TPS10":
         self.verticalSliderTPS1.setValue(int(self.lineEditTPS1.text()))
         TPS10Value0=self.lineEditTPS1.text()
         print(TPS10Value0)

      # if event=="TPS11":
      #    CTSValue1=self.lineEditCTS.setText(str(self.verticalSliderCTS.value()))
      #    print(CTSValue1)
   
      if event=="Uo2S0":
         self.verticalSliderUO2S.setValue(int(self.lineEditUo2S.text()))
         CTSValue0=self.lineEditUo2S.text()
         print(CTSValue0)

      # if event=="Uo2S1":
      #    CTSValue1=self.lineEditCTS.setText(str(self.verticalSliderCTS.value()))
      #    print(CTSValue1)

      # if event=="TPS2":
         self.verticalSliderCTS.setValue(int(self.lineEditCTS.text()))
         CTSValue0=self.lineEditCTS.text()
         print(CTSValue0)

      # if event=="TPS2":
      #    CTSValue1=self.lineEditCTS.setText(str(self.verticalSliderCTS.value()))
      #    print(CTSValue1)

      # if event=="MAT0":
         self.verticalSliderCTS.setValue(int(self.lineEditCTS.text()))
         CTSValue0=self.lineEditCTS.text()
         print(CTSValue0)

      # if event=="MAT1":
      #     CTSValue0=self.verticalSliderCTS.setValue(int(self.lineEditCTS.text()))
      #     print(CTSValue0)

      # if event=="Reserve10":
         self.verticalSliderCTS.setValue(int(self.lineEditCTS.text()))
         CTSValue0=self.lineEditCTS.text()
         print(CTSValue0)

      # if event=="Reserve11":
         self.verticalSliderCTS.setValue(int(self.lineEditCTS.text()))
         CTSValue0=self.lineEditCTS.text()
         print(CTSValue0)
























      

         




   def ConnectSerial(self):
      print('salam')
      # com = self.comboBox.currentText()
      # com = com[com.find('COM'):com.find('COM')+4]#select only COM# from whole text, u need to put com# in next line
      # self.ser = serial.Serial(
      #     port = com,#u can pu any com u want here for example "COM4" or "COM3". it need to be string
      #     baudrate = 9600,
      #     parity = serial.PARITY_NONE,
      #     stopbits = serial.STOPBITS_ONE,
      #     bytesize = serial.EIGHTBITS,
      #     timeout = 100)
      # if self.ser.isOpen():# returns true if port was open
      #     self.DisEnable(True)
      
   def DisconnectSerial(self):
      print('bybye')
      # self.ser.close()
      # if not self.ser.isOpen():
      #     self.DisEnable(False)

   # def DisEnable(self, mode):#this function will change buttons and combobox state with opening and closing com port 
   #     if mode:
   #         self.btnConnect.setDisabled(mode)
   #         self.comboBox.setDisabled(mode)
   #         self.btnSend.setEnabled(mode)
   #         self.btnDisconnect.setEnabled(mode)
   #     else:
   #         self.btnConnect.setEnabled(~mode)
   #         self.comboBox.setEnabled(~mode)
   #         self.btnSend.setDisabled(~mode)
   #         self.btnDisconnect.setDisabled(~mode)

   def SendSerial(self):
      print("hoora")
      # self.ser.write(self.Message) #u should update your message content before send

   # def CreateByte(self, bit0, bit1, bit2, bit3, bit4, bit5, bit6, bit7):#just a sample funtion for creating byte from bits
   #     return  bit0 | bit1<<1 | bit2<<2  | bit3 << 3 | bit4 << 4 | bit5 << 5 | bit6 << 6 | bit7 << 7   

      

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())