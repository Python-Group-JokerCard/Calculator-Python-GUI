#!/usr/bin/python3
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(434, 298)
        MainWindow.setFixedSize(434, 298)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Entry = QtWidgets.QTextEdit(self.centralwidget)
        self.Entry.setGeometry(QtCore.QRect(20, 10, 361, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.Entry.setFont(font)
        self.Entry.setObjectName("Entry")
        self.Entry.setReadOnly(True)
        self.number7 = QtWidgets.QPushButton(self.centralwidget)
        self.number7.setGeometry(QtCore.QRect(20, 90, 88, 27))
        self.number7.setObjectName("number7")
        self.number8 = QtWidgets.QPushButton(self.centralwidget)
        self.number8.setGeometry(QtCore.QRect(110, 90, 88, 27))
        self.number8.setObjectName("number8")
        self.number9 = QtWidgets.QPushButton(self.centralwidget)
        self.number9.setGeometry(QtCore.QRect(200, 90, 88, 27))
        self.number9.setObjectName("number9")
        self.sum = QtWidgets.QPushButton(self.centralwidget)
        self.sum.setGeometry(QtCore.QRect(290, 90, 88, 27))
        self.sum.setObjectName("sum")
        self.number4 = QtWidgets.QPushButton(self.centralwidget)
        self.number4.setGeometry(QtCore.QRect(20, 130, 88, 27))
        self.number4.setObjectName("number4")
        self.number5 = QtWidgets.QPushButton(self.centralwidget)
        self.number5.setGeometry(QtCore.QRect(110, 130, 88, 27))
        self.number5.setObjectName("number5")
        self.number6 = QtWidgets.QPushButton(self.centralwidget)
        self.number6.setGeometry(QtCore.QRect(200, 130, 88, 27))
        self.number6.setObjectName("number6")
        self.subtraction = QtWidgets.QPushButton(self.centralwidget)
        self.subtraction.setGeometry(QtCore.QRect(290, 130, 88, 27))
        self.subtraction.setObjectName("subtraction")
        self.number1 = QtWidgets.QPushButton(self.centralwidget)
        self.number1.setGeometry(QtCore.QRect(20, 170, 88, 27))
        self.number1.setObjectName("number1")
        self.number2 = QtWidgets.QPushButton(self.centralwidget)
        self.number2.setGeometry(QtCore.QRect(110, 170, 88, 27))
        self.number2.setObjectName("number2")
        self.multiply = QtWidgets.QPushButton(self.centralwidget)
        self.multiply.setGeometry(QtCore.QRect(290, 170, 88, 27))
        self.multiply.setObjectName("multiply")
        self.number3 = QtWidgets.QPushButton(self.centralwidget)
        self.number3.setGeometry(QtCore.QRect(200, 170, 88, 27))
        self.number3.setObjectName("number3")
        self.divide = QtWidgets.QPushButton(self.centralwidget)
        self.divide.setGeometry(QtCore.QRect(290, 210, 88, 27))
        self.divide.setObjectName("divide")
        self.erase = QtWidgets.QPushButton(self.centralwidget)
        self.erase.setGeometry(QtCore.QRect(200, 210, 88, 27))
        self.erase.setObjectName("erase")
        self.number0 = QtWidgets.QPushButton(self.centralwidget)
        self.number0.setGeometry(QtCore.QRect(110, 210, 88, 27))
        self.number0.setObjectName("number0")
        self.dot = QtWidgets.QPushButton(self.centralwidget)
        self.dot.setGeometry(QtCore.QRect(20, 210, 88, 27))
        self.dot.setObjectName("dot")
        self.operators = QtWidgets.QTextEdit(self.centralwidget)
        self.operators.setGeometry(QtCore.QRect(390, 20, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.operators.setFont(font)
        self.operators.setObjectName("operators")
        self.operators.setReadOnly(True)
        self.equls = QtWidgets.QPushButton(self.centralwidget)
        self.equls.setGeometry(QtCore.QRect(390, 140, 41, 91))
        self.equls.setObjectName("equls")
        self.ce = QtWidgets.QPushButton(self.centralwidget)
        self.ce.setGeometry(QtCore.QRect(390, 100, 41, 41))
        self.ce.setObjectName("ce")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 434, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.number0.clicked.connect(self.zero)
        self.number1.clicked.connect(self.one)
        self.number2.clicked.connect(self.two)
        self.number3.clicked.connect(self.three)
        self.number4.clicked.connect(self.four)
        self.number5.clicked.connect(self.five)
        self.number6.clicked.connect(self.six)
        self.number7.clicked.connect(self.seven)
        self.number8.clicked.connect(self.eight)
        self.number9.clicked.connect(self.nine)
        self.dot.clicked.connect(self.dott)
        self.subtraction.clicked.connect(self.subtractionn)
        self.divide.clicked.connect(self.dividee)
        self.multiply.clicked.connect(self.multiplyy)
        self.sum.clicked.connect(self.summ)
        self.erase.clicked.connect(self.erasee)    
        self.equls.clicked.connect(self.equlss)
        self.ce.clicked.connect(self.cee)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.Entry.insertPlainText('0')
        num1 = 0

    
    def zero(self):
        if self.Entry.toPlainText() == '':
            self.Entry.insertPlainText('0')
        elif self.Entry.toPlainText() == '0':
            None
        else:
            self.Entry.insertPlainText('0')        
    def one(self):
        if self.Entry.toPlainText() == '0':
            self.Entry.clear()
            self.Entry.insertPlainText('1')
        else:
            self.Entry.insertPlainText('1')    
    def two(self):
        if self.Entry.toPlainText() == '0':
            self.Entry.clear()
            self.Entry.insertPlainText('2')
        else:
            self.Entry.insertPlainText('2') 
    def three(self):
        if self.Entry.toPlainText() == '0':
            self.Entry.clear()
            self.Entry.insertPlainText('3')
        else:
            self.Entry.insertPlainText('3')   
    def four(self):
        if self.Entry.toPlainText() == '0':
            self.Entry.clear()
            self.Entry.insertPlainText('4')
        else:
            self.Entry.insertPlainText('4')        
    def five(self):
        if self.Entry.toPlainText() == '0':
            self.Entry.clear()
            self.Entry.insertPlainText('5')
        else:
            self.Entry.insertPlainText('5') 
    def six(self):
        if self.Entry.toPlainText() == '0':
            self.Entry.clear()
            self.Entry.insertPlainText('6')
        else:
            self.Entry.insertPlainText('6')     
    def seven(self):
        if self.Entry.toPlainText() == '0':
            self.Entry.clear()
            self.Entry.insertPlainText('7')
        else:
            self.Entry.insertPlainText('7') 
    def eight(self):
        if self.Entry.toPlainText() == '0':
            self.Entry.clear()
            self.Entry.insertPlainText('8')
        else:
            self.Entry.insertPlainText('8') 
    def nine(self):
        if self.Entry.toPlainText() == '0':
            self.Entry.clear()
            self.Entry.insertPlainText('9')
        else:
            self.Entry.insertPlainText('9') 
    def dott(self):
        if '.' in self.Entry.toPlainText():
            None
        elif self.Entry.toPlainText() == '':
            None
        else:        
            self.Entry.insertPlainText('.')
        #self.dot.setEnabled(False)
    def summ(self):
        global num1
        num1 = float(self.Entry.toPlainText())
        if self.operators.toPlainText() == '+'or'-'or'x'or'/':
            self.operators.clear()
            self.operators.insertPlainText('+')
        else:
            self.operators.insertPlainText('+')
        self.Entry.clear()
        self.Entry.insertPlainText('0')    
    def multiplyy(self):
        global num1
        num1 = float(self.Entry.toPlainText())
        if self.operators.toPlainText() == '+'or'-'or'x'or'/':
            self.operators.clear()
            self.operators.insertPlainText('x')
        else:    
            self.operators.insertPlainText('x')
        self.Entry.clear() 
        self.Entry.insertPlainText('0')   
    def dividee(self):
        global num1
        num1 = float(self.Entry.toPlainText())
        if self.operators.toPlainText() == '+'or'-'or'x'or'/':
            self.operators.clear()
            self.operators.insertPlainText('/')
        else:
            self.operators.insertPlainText('/')
        self.Entry.clear()  
        self.Entry.insertPlainText('0')  
    def subtractionn(self):
        global num1
        num1 = float(self.Entry.toPlainText())
        if self.operators.toPlainText() == '+'or'-'or'x'or'/':
            self.operators.clear()
            self.operators.insertPlainText('-')
        else:    
            self.operators.insertPlainText('-') 
        self.Entry.clear()
        self.Entry.insertPlainText('0')    
    def erasee(self):
        if self.Entry.toPlainText() == '0':
            None
        elif len(self.Entry.toPlainText()) == 1:
            self.Entry.clear()
            self.operators.clear()
            self.Entry.insertPlainText('0')    
        else:    
            valu = self.Entry.toPlainText() 
            valu = valu[:-1]
            self.Entry.clear()
            self.Entry.append(valu) 
            self.operators.clear()
    def cee(self):
        if self.Entry.toPlainText() == '0':
            self.operators.clear()
        else:    
            self.Entry.clear() 
            self.operators.clear()
            self.Entry.insertPlainText('0')   

    def equlss(self):
        global num1
        num2 = float(self.Entry.toPlainText())
        self.Entry.clear()
        if self.operators.toPlainText() == '':
            pass
        elif self.operators.toPlainText() == '+':
            num3 = str(num1 + num2)
            if num3.endswith('.0'):
                num3 = num3[:-2]
            self.Entry.insertPlainText(num3)
        elif self.operators.toPlainText()== '-':
            num3 = str(num1 - num2)
            if num3.endswith('.0'):
                num3 = num3[:-2]
            self.Entry.insertPlainText(num3) 
        elif self.operators.toPlainText() == 'x':
            num3 = str(num1 * num2)
            if num3.endswith('.0'):
                num3 = num3[:-2]
            self.Entry.insertPlainText(num3)    
        elif self.operators.toPlainText() == '/':
            try:
                num3 = str(num1 / num2)
                if num3.endswith('.0'):
                    num3 = num3[:-2]
                self.Entry.insertPlainText(num3)
            except:
                num3 = '0'
                self.Entry.insertPlainText(num3)        
        else:
            None
        if self.Entry.toPlainText() == '':
            self.Entry.insertPlainText('0')
        else:
            None        
        if self.Entry.toPlainText() != '':  
            if self.operators.toPlainText() != '':  
                num1 = float(self.Entry.toPlainText())
        else:
            pass    


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculater"))
        self.Entry.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:24pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.number7.setText(_translate("MainWindow", "7"))
        self.number7.setShortcut(_translate("MainWindow", "7"))
        self.number8.setText(_translate("MainWindow", "8"))
        self.number8.setShortcut(_translate("MainWindow", "8"))
        self.number9.setText(_translate("MainWindow", "9"))
        self.number9.setShortcut(_translate("MainWindow", "9"))
        self.sum.setText(_translate("MainWindow", "+"))
        self.sum.setShortcut(_translate("MainWindow", "+"))
        self.number4.setText(_translate("MainWindow", "4"))
        self.number4.setShortcut(_translate("MainWindow", "4"))
        self.number5.setText(_translate("MainWindow", "5"))
        self.number5.setShortcut(_translate("MainWindow", "5"))
        self.number6.setText(_translate("MainWindow", "6"))
        self.number6.setShortcut(_translate("MainWindow", "6"))
        self.subtraction.setText(_translate("MainWindow", "-"))
        self.subtraction.setShortcut(_translate("MainWindow", "-"))
        self.number1.setText(_translate("MainWindow", "1"))
        self.number1.setShortcut(_translate("MainWindow", "1"))
        self.number2.setText(_translate("MainWindow", "2"))
        self.number2.setShortcut(_translate("MainWindow", "2"))
        self.multiply.setText(_translate("MainWindow", "x"))
        self.multiply.setShortcut(_translate("MainWindow", "*"))
        self.number3.setText(_translate("MainWindow", "3"))
        self.number3.setShortcut(_translate("MainWindow", "3"))
        self.divide.setText(_translate("MainWindow", "/"))
        self.divide.setShortcut(_translate("MainWindow", "/"))
        self.erase.setText(_translate("MainWindow", "<--"))
        self.erase.setShortcut(_translate("MainWindow", "Backspace"))
        self.number0.setText(_translate("MainWindow", "0"))
        self.number0.setShortcut(_translate("MainWindow", "0"))
        self.dot.setText(_translate("MainWindow", "."))
        self.dot.setShortcut(_translate("MainWindow", "."))
        self.operators.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:14pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; font-weight:400;\"><br /></p></body></html>"))
        self.equls.setText(_translate("MainWindow", "="))
        self.equls.setShortcut(_translate("MainWindow", "Enter"))
        self.ce.setText(_translate("MainWindow", "CE"))
        self.ce.setShortcut(_translate("MainWindow", "Shift+Del"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
