# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from mlx90614 import MLX90614
import max30100
import time
import sys
import json

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(974, 757)
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(48)
        font.setItalic(False)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 971, 80))
        self.groupBox.setStyleSheet("background-color: rgb(6, 99, 157);")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(430, 10, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.TextBox = QtWidgets.QGroupBox(self.centralwidget)
        self.TextBox.setGeometry(QtCore.QRect(10, 190, 951, 151))
        self.TextBox.setStyleSheet("background-color: white;")
        self.TextBox.setTitle("")
        self.TextBox.setObjectName("TextBox")
        self.TextView = QtWidgets.QLabel(self.TextBox)
        self.TextView.setGeometry(QtCore.QRect(160, 10, 691, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.TextView.setFont(font)
        self.TextView.setStyleSheet("")
        self.TextView.setObjectName("TextView")
        self.SensorValue = QtWidgets.QLabel(self.TextBox)
        self.SensorValue.setGeometry(QtCore.QRect(400, 70, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.SensorValue.setFont(font)
        self.SensorValue.setObjectName("SensorValue")
        self.SignView = QtWidgets.QLabel(self.TextBox)
        self.SignView.setGeometry(QtCore.QRect(500, 70, 41, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.SignView.setFont(font)
        self.SignView.setObjectName("SignView")
        self.BodyTempButton = QtWidgets.QPushButton(self.centralwidget)
        self.BodyTempButton.setGeometry(QtCore.QRect(40, 360, 391, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.BodyTempButton.setFont(font)
        self.BodyTempButton.setStyleSheet("QPushButton"
                             "{"
                             "background-color :  rgb(186, 201, 192);"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color: rgb(115, 122, 118);"
                             "}")
        self.BodyTempButton.setObjectName("BodyTempButton")
        self.SPButton = QtWidgets.QPushButton(self.centralwidget)
        self.SPButton.setGeometry(QtCore.QRect(40, 430, 391, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.SPButton.setFont(font)
        self.SPButton.setStyleSheet("QPushButton"
                             "{"
                             "background-color :  rgb(186, 201, 192);"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color: rgb(115, 122, 118);"
                             "}")
        self.SPButton.setObjectName("SPButton")
        self.HRButton = QtWidgets.QPushButton(self.centralwidget)
        self.HRButton.setGeometry(QtCore.QRect(540, 360, 391, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.HRButton.setFont(font)
        self.HRButton.setStyleSheet("QPushButton"
                             "{"
                             "background-color :  rgb(186, 201, 192);"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color: rgb(115, 122, 118);"
                             "}")
        self.HRButton.setObjectName("HRButton")
        self.WelcomeBox = QtWidgets.QGroupBox(self.centralwidget)
        self.WelcomeBox.setGeometry(QtCore.QRect(320, 110, 351, 71))
        self.WelcomeBox.setStyleSheet("background-color: rgb(254, 220, 151);")
        self.WelcomeBox.setTitle("")
        self.WelcomeBox.setObjectName("WelcomeBox")
        self.WelcomeLabel = QtWidgets.QLabel(self.WelcomeBox)
        self.WelcomeLabel.setGeometry(QtCore.QRect(60, 20, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.WelcomeLabel.setFont(font)
        self.WelcomeLabel.setObjectName("WelcomeLabel")
        self.Prescription_Box = QtWidgets.QGroupBox(self.centralwidget)
        self.Prescription_Box.setGeometry(QtCore.QRect(10, 520, 951, 171))
        self.Prescription_Box.setTitle("")
        self.Prescription_Box.setObjectName("Prescription_Box")
        self.Prescription_Button = QtWidgets.QPushButton(self.Prescription_Box)
        self.Prescription_Button.setGeometry(QtCore.QRect(720, 120, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Prescription_Button.setFont(font)
        self.Prescription_Button.setStyleSheet("QPushButton"
                             "{"
                             "background-color :  rgb(186, 201, 192);"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color: rgb(115, 122, 118);"
                             "}")
        self.Prescription_Button.setObjectName("Prescription_Button")
        self.Prescription_Text = QtWidgets.QLabel(self.Prescription_Box)
        self.Prescription_Text.setGeometry(QtCore.QRect(20, 10, 921, 71))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.Prescription_Text.setFont(font)
        self.Prescription_Text.setObjectName("Prescription_Text")
        self.ExitButton = QtWidgets.QPushButton(self.centralwidget)
        self.ExitButton.setGeometry(QtCore.QRect(540, 430, 391, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.ExitButton.setFont(font)
        self.ExitButton.setStyleSheet("QPushButton"
                             "{"
                             "background-color :  rgb(186, 201, 192);"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color: rgb(115, 122, 118);"
                             "}")
        self.ExitButton.setObjectName("ExitButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 974, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
       
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "e-DOC "))
        self.TextView.setText(_translate("MainWindow", "                       "))
        self.SensorValue.setText(_translate("MainWindow", ""))
        self.SignView.setText(_translate("MainWindow", ""))
        self.BodyTempButton.setText(_translate("MainWindow", "Check Body Temperature"))
        self.SPButton.setText(_translate("MainWindow", "Check Spo2"))
        self.HRButton.setText(_translate("MainWindow", "Check Heart Rate"))
        self.ExitButton.setText(_translate("MainWindow", "Send Data"))
        self.Prescription_Button.setText(_translate("MainWindow", "View Prescription"))
        self.WelcomeLabel.setText(_translate("MainWindow", "   Welcome User!"))
        self.Prescription_Text.setText(_translate("MainWindow", "Click Below to view Prescription."))
        self.force_close=True
        self.BodyTempButton.clicked.connect(self.run)
        self.HRButton.clicked.connect(self.calcHR)
        self.SPButton.clicked.connect(self.calcSP)
        self.ExitButton.clicked.connect(self.closing)
        self.Prescription_Button.clicked.connect(self.viewPres)

    def run(self):
        
        thermometer_address = 0x5a

        thermometer = MLX90614(thermometer_address)
        values=[0]*10
        i=0
        sum1=0
        time.sleep(2)
     
        self.WelcomeBox.setStyleSheet("background-color: rgb(254, 220, 151);")
        self.TextView.setText("Kindly wait while the device calculates the result.")
        
        while (i<3):
            time.sleep(2)
            l = thermometer.get_obj_temp()
   
            time.sleep(1)
            sum1=sum1+l
            i=i+1
   
        avg=sum1/3
        body_temp= ((avg*(9/5))+32)
        if body_temp>102:
                    body_temp=body_temp-3
        self.TextView.setText("                                 Body Temperature")
        self.SensorValue.setText(str(round(body_temp,2)))
        self.SignView.setText("°F")

    def calcHR(self):
        time.sleep(3)
        self.WelcomeBox.setStyleSheet("background-color: rgb(254, 220, 151);")
        
        try:
            mx30 = max30100.MAX30100()
            i = 0
            x=0
            VAL_HR=[0]*5
            while i < 3:
                time.sleep(1)
                mx30 = max30100.MAX30100()
                mx30.reinit()
                mx30.set_mode(max30100.MODE_SPO2)
                time.sleep(1)

                mx30.read_sensor()
                
                if mx30.ir>0:
                    VAL_HR[i]= mx30.ir
                    x=x+1
                mx30.reset()
                time.sleep(1)

                i = i + 1
            
            maxhr=max(VAL_HR)
            self.TextView.setText("                                           Heart Rate ")
            self.SensorValue.setText(str(int(maxhr/100)+10))
            self.SignView.setText("bpm") 
            mx30.reset()
            mx30.shutdown()


        except Exception as e:
            print("Max30100 got exception {}".format(e))

    def calcSP(self):
        self.WelcomeBox.setStyleSheet("background-color: rgb(254, 220, 151);")
    
        try:
            mx30 = max30100.MAX30100()
            i = 0
            x=0
            VAL_SP=[0]*5
            while i < 3:
                time.sleep(1)
                mx30 = max30100.MAX30100()
                mx30.reinit()
                mx30.set_mode(max30100.MODE_SPO2)
                time.sleep(1)

                mx30.read_sensor()
                       
                l=mx30.red
                if l > 8000:
                    if l >10000:
                        l=l-1000
                    VAL_SP[i]= l
                    x=x+1
                mx30.reset()
                time.sleep(1)

                i = i + 1
        
            maxval=max(VAL_SP)
            self.TextView.setText("                                              SpO2")
            #self.SensorValue.setText(str(avg))
            self.SensorValue.setText(str(maxval/100))
            self.SignView.setText("%")
            mx30.reset()
            mx30.shutdown()


        except Exception as e:
            print("Max30100 got exception {}".format(e))
            
    def viewPres(self):
        with open('edoc.json') as f:
          data = json.load(f)
       
        self.Prescription_Text.setText(data)
        

    def closing(self):
       
        self.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

