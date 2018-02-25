f = open("file1.py", "w")  # 打开文件
f.write('print (898989)')
f.close()  #关闭文件
import os

b=os.getcwd()
print (type(b))
qiemulu='cd '+b
print (qiemulu)
a=os.system(qiemulu)
#这个system模块如果返回是0就是正确,其他数就是错误
os.system(qiemulu)
os.system('calc')


a=os.system("python file1.py")
os.system('pause')
print(a)



