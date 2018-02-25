
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtWidgets  
from PyQt5.QtWidgets import QFileDialog
import codecs
class MyWindow(QWidget):  
    def __init__(self):
        
        super().__init__()
        
        self.resize(800,800)
        self.myButton = QtWidgets.QPushButton(self)  
        self.myButton.setObjectName("myButton")  
        self.myButton.setText("Open")  
        self.myButton.clicked.connect(self.load)  
        self.myButton2 = QtWidgets.QPushButton(self)  
        self.myButton2.setObjectName("myButton")  
        self.myButton2.setText("save")  
        self.myButton2.clicked.connect(self.save)
        self.myButton2.move(200,0)



        self.textEdit = QtWidgets.QTextEdit(self)
        self.textEdit.setGeometry(QtCore.QRect(10, 40, 801, 521))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.resize(1500,600)


#write something
        self.textEdit.insertPlainText('32423423423')
        #下面就是用html语言来插入图片
##        self.textEdit.insertHtml('<img src=1.png>' )

        #用html来保存就行了,利用下面4行测试了一下效果不错.
##        a=self.textEdit.toHtml()
##        self.textEdit.insertPlainText('32423423423')
##        self.textEdit.insertPlainText('32423423423')
##        self.textEdit.setHtml(a)

        
    def load(self):  
        
        fileName1, filetype = QFileDialog.getOpenFileName(self,  
                                    "选取文件",  
                                    "C:/",  
                                    "Text Files (*.txt)")   #设置文件扩展名过滤,注意用双分号间隔  
        print (fileName1,filetype)

    def save(self):
        fileName2, ok2 = QFileDialog.getSaveFileName(self,  
                                    "文件保存",  
                                    "C:/",  
                                    "All Files (*);;Text Files (*.txt)")  

        a=self.textEdit.toPlainText()
        
        
####        file = open(self.filename2, 'w', 'utf-8')
##        file = codecs.open(self.filename2, 'w', 'utf-8')
##        file.write(a)
##        file.close()



        f=open(self.filename2, 'w')
        exit()
        
        pickle.dump(a,f,0)  
        f.close()  
                



        
  
if __name__=="__main__":    
    import sys    
    
    app=QtWidgets.QApplication(sys.argv)    
    myshow=MyWindow()  
    myshow.show()  
    sys.exit(app.exec_()) 
