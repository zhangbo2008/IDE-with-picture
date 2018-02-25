# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '编辑器.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtWidgets  
from PyQt5.QtWidgets import QFileDialog  
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1954, 1787)
        







        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(30, 30, 112, 34))
        self.pushButton.setObjectName("open")
        self.pushButton.move(200,800)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 30, 112, 34))
        self.pushButton_2.setObjectName("close")
        self.pushButton_2.move(500,800)





        
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(100, 40, 801, 521))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.resize(1500,600)
        #用下面这行来输入内容
        self.textEdit.insertPlainText('32423423423')
        #下面就是用html语言来插入图片
        self.textEdit.insertHtml('<img src=1.png>' )
##        a=1
##        self.textEdit.insertHtml(a)
        #用html来保存就行了,利用下面4行测试了一下效果不错.
        a=self.textEdit.toHtml()
        self.textEdit.insertPlainText('32423423423')
        self.textEdit.insertPlainText('32423423423')
        self.textEdit.setHtml(a)


        
        
        
        self.pushButton.clicked.connect(self.loadFile)  
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.show()


    def loadFile(self):########载入file
        
        fileName1, filetype = QFileDialog.getOpenFileName(self,  
                                    "选取文件",  
                                    "C:/",  
                                    "All Files (*);;Text Files (*.txt)")         ##"open file Dialog "文件对话框的标题，第二个是打开的默认路径，第三个是文件类型
        self.loadFileLineEdit.setText(file_name)

    def saveFile(self):
        a=self.textEdit.toHtml()
        file_path =  QFileDialog.getSaveFileName(self,'save file',"saveFile" ,"xj3dp files (*.xj3dp);;all files(*.*)") 
        

    












        
        
        
                     

#就在这里记录下我需要的东西,这个格式textEdit控件,叫富文本,他是微软的写字板rtf.
#里面随便输入图片和文字
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "IDE with picture"))
        self.pushButton.setText(_translate("Dialog", "open"))
        self.pushButton_2.setText(_translate("Dialog", "close"))
    


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    widget = QWidget(None)
    Ui_Dialog().setupUi(widget)
    sys.exit(app.exec_())
    pass










