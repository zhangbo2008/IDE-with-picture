f = open("file1.py", "w")  # 打开文件
f.write('print (898989)')
f.close()  #关闭文件
import os

b=os.getcwd()

qiemulu='cd '+b

a=os.system(qiemulu)
#这个system模块如果返回是0就是正确,其他数就是错误
os.system(qiemulu)


#现在只能这样用这个方式调用回python自带的ide里面
a=os.system("python file1.py")
os.system("file1.py")

print(a)



