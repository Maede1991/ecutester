import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2 import QtWidgets
from PySide2.QtCore import QFile
from mainwindow import Ui_MainWindow
from PySide2 import QtCore, QtWidgets, QtSerialPort
import serial
import serial.tools.list_ports






class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.Message = bytearray(32) #defining a variable with 32 bytes of data, if u want to change bits u need to use shift and | and & operators
        self.Message[0] = 0xFF
        self.lineEditCTS.returnPressed.connect(lambda:self.text_changed("CTS0"))#event active with enter key
        self.lineEditDo2S.returnPressed.connect(lambda:self.text_changed("Do2S"))
        self.lineEditFuelLevel.returnPressed.connect(lambda:self.text_changed("FuelLevel"))
        self.lineEditMAP.returnPressed.connect(lambda:self.text_changed("MAP"))
        self.lineEditMAT.returnPressed.connect(lambda:self.text_changed("MAT"))
        self.lineEditPVS1.returnPressed.connect(lambda:self.text_changed("PVS1"))
        self.lineEditPVS2.returnPressed.connect(lambda:self.text_changed("PVS2"))
        self.lineEditRPM.returnPressed.connect(lambda:self.text_changed("RPM"))
        self.lineEditSPEED.returnPressed.connect(lambda:self.text_changed("SPEED"))
        self.lineEditTPS1.returnPressed.connect(lambda:self.text_changed("TPS1"))
        self.lineEditTPS2.returnPressed.connect(lambda:self.text_changed("TPS2"))
        self.lineEditUo2S.returnPressed.connect(lambda:self.text_changed("Uo2S"))
        self.lineEditReserve1.returnPressed.connect(lambda:self.text_changed("Reserve1"))
        self.lineEditReserve2.returnPressed.connect(lambda:self.text_changed("Reserve2"))


        self.verticalSliderCTS.valueChanged.connect(lambda:self.text_changed("CTS1"))
        self.verticalSliderFUELLEVEL.sliderMoved.connect(lambda:self.text_changed("FUELLEVEL"))






       # self.Message[1] = self.CreateByte(1, 0, 1, 0, 1, 0, 0, 1)#set 8 bits in one byte
        #self.DisEnable(False)
        self.btnConnect.clicked.connect(self.ConnectSerial)
        self.btndisconnect.clicked.connect(self.DisconnectSerial)
       # self.lineEdit.setInputMask("0x-HH");
        #self.btnSend.clicked.connect(lambda : self.ser.write(self.Message)) u can use this instead of defining function
        self.btnSendData.clicked.connect(self.SendSerial)
        # Ports = serial.tools.list_ports.comports() # make a list from available COM ports. u should print this to see whole list
        # for this in Ports:
        #     #com = str(this)
        #     #self.comboBox.addItem(com[com.find('COM'):com.find('COM')+5])
        #     self.comboBoxCOM.addItem(str(this))




    def text_changed(self,event):
        if event=="CTS0":
            CTSValue0=self.verticalSliderCTS.setVisible(int(self.lineEditCTS.text()))
            print(CTSValue0)

        if event=="CTS1":
           CTSValue1=self.lineEditCTS.setText(str(self.verticalSliderCTS.value()))
           print(CTSValue1)

        if event=="Do2S":
            Do2SValue=self.lineEditDo2S.text()
            print(Do2SValue)    

        if event=="FuelLevel":
            FuelLevelValue=self.lineEditFuelLevel.text()
            print(FuelLevelValue) 

        if event=="MAP":
            MAPValue=self.lineEditMAP.text()
            print(MAPValue)

        if event=="PVS1":
            PVS1Value=self.lineEditPVS1.text()
            print(PVS1Value)    

        if event=="PVS2":
            PVS2Value=self.lineEditPVS2.text()
            print(PVS2Value) 

        if event=="RPM":
            RPMValue=self.lineEditRPM.text()
            print(RPMValue)

        if event=="SPEED":
            SPEEDValue=self.lineEditSPEED.text()
            print(SPEEDValue)    

        if event=="TPS1":
            TPS1Value=self.lineEditTPS1.text()
            print(TPS1Value) 

        if event=="Uo2S":
            Uo2SValue=self.lineEditUo2S.text()
            print(Uo2SValue)

        if event=="TPS2":
            TPS2Value=self.lineEditTPS2.text()
            print(TPS2Value) 

        if event=="MAT":
            MATValue=self.lineEditMAT.text()
            print(MATValue)

        if event=="Reserve1":
            Reserve1Value=self.lineEditReserve1.text()
            print(Reserve1Value)    

        if event=="Reserve2":
            Reserve2Value=self.lineEditReserve2.text()
            print(Reserve2Value)               
            
    
            




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