
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
#!/usr/bin/python3
# -*- coding: utf-8 -*-
 
"""
Py40 PyQt5 tutorial 
 
This program creates a statusbar.
 
author: Jan Bodnar
website: py40.com 
last edited: January 2015
"""
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
def save(self):
        f.open('a23.txt','w')
        exit()
        
        f.write(3423)
        f.close()
 
class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.resize(8000,8000)
        self.myButton = QtWidgets.QPushButton(self)  
        self.myButton.setObjectName("myButton")  
        self.myButton.setText("Open")  
##        self.myButton.clicked.connect(self.load)  
        self.myButton2 = QtWidgets.QPushButton(self)  
        self.myButton2.setObjectName("myButton")  
        self.myButton2.setText("save")  
        self.myButton2.clicked.connect(save)
        self.myButton2.move(200,0)
        self.myButton3 = QtWidgets.QPushButton(self)  
        self.myButton3.setObjectName("myButton")  
        self.myButton3.setText("run")  
##        self.myButton3.clicked.connect(self.run)
        self.myButton3.move(400,0)
        self.initUI()

        
    def initUI(self):               
        
        self.statusBar().showMessage('Ready')
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Statusbar')    
        self.show()
        
 
 
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
