from PyQt5 import QtWidgets  
from PyQt5.QtWidgets import QFileDialog  
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtWidgets  
from PyQt5.QtWidgets import QFileDialog
import codecs
import sys
import os
def i(a,*arg):
    f=open(a,'w')
    print (arg)
    f.write(88888)
    f.close()
    pass
class MyWindow(QtWidgets.QWidget):  
    def __init__(self):  
        super(MyWindow,self).__init__()
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
        self.myButton3 = QtWidgets.QPushButton(self)  
        self.myButton3.setObjectName("myButton")  
        self.myButton3.setText("run")  
        self.myButton3.clicked.connect(self.run)
        self.myButton3.move(400,0)



        self.textEdit = QtWidgets.QTextEdit(self)
        self.textEdit.setGeometry(QtCore.QRect(10, 40, 801, 521))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.resize(1500,600)


#write something
        self.textEdit.insertPlainText('print (42389)')
        #下面就是用html语言来插入图片
        self.textEdit.insertHtml('<img src=1.png>' )

        #用html来保存就行了,利用下面4行测试了一下效果不错.
        
        
        
        
        

        
    def load(self):  
        
        fileName1, filetype = QFileDialog.getOpenFileName(self,  
                                    "选取文件",  
                                    "C:/",  
                                    "Text Files (*.txt)")   #设置文件扩展名过滤,注意用双分号间隔  
        #read就是全读取这些都好使
        text=open(fileName1,'r').read()
        print (text)
        self.textEdit.setText(text)
        i()
    def save(self):
        fileName2, ok2 = QFileDialog.getSaveFileName(self,  
                                    "文件保存",  
                                    "C:/",  
                                    "All Files (*);;Text Files (*.txt)")
        print (fileName2,ok2)
        my_text=self.textEdit.toHtml()
        print (my_text)
##        print (my_text)
        i(fileName2,my_text)
##        a=self.textEdit.toHtml()
##        file = open(filename2, 'w')
##        #这下面的write也不能跑
##        file.write(unicode(a))
##        file.close()
        #实在受不了这个save函数,it raise error whenever i use write command,i find out to make a function saveout
        
        
        

##        my_text=self.textEdit.toPlainText()
##        print (my_text)#这东西打印出来最后多一个obj是什么鬼,别人为什么好使??
##                        #试了半天还是不行,即使我把图片给删除了也不行.
##        filename=QFileDialog.getSaveFileName(self,'save file','C:/',"Text Files (*.txt)")
##        print (filename)
##        
##        
##        f=open(filename[0],'w')
##        
##        #就是下面的write出的毛病
##        print (my_text)
##        my_text=str(my_text)
##        print (my_text)
##        f.write(my_text)
##        f.close()#跟写的内容没关系,write什么都报错.








        
    def run(self):
        
        a=self.textEdit.toPlainText()
        
        
        f = open("file1.py", "w")  # 打开文件
        
        #下面这行write写不了??为什么是不是qt模块冲突
        f.write(a)
        exit()
        
        f.close()  #关闭文件
        

        b=os.getcwd()

        qiemulu='cd '+b

        a=os.system(qiemulu)
        #这个system模块如果返回是0就是正确,其他数就是错误
        os.system(qiemulu)


        #现在只能这样用这个方式调用回python自带的ide里面
        a=os.system("python file1.py")
        os.system("file1.py")





        
##        print (a)
##        print (type(a))
##        file = open('.\run.txt', 'w', 'utf-8')
##        
##        print (66)
##        file.write((a))
##        exit()
##        
##        file.close()  



        
  
if __name__=="__main__":    
        
    f = open("file3.py", "w")  # 打开文件
    
    #下面这行write写不了??为什么是不是qt模块冲突
    f.write('32131231111111111111111111')
    f.close()
    print (4324)

    app=QtWidgets.QApplication(sys.argv)    
    myshow=MyWindow()  
    myshow.show()  
    sys.exit(app.exec_()) 
