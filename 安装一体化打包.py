#将多个程序文件生成一个.py文件(不支持文件夹)
#实现二次打包程序
import os
def installpy(path,topath=os.getcwd()+'\\',exe_name='install.py'):#(自定义打包原目录,打包目标文件夹，安装包名称）
    path+='\\'
    #预设语句
    part_1=r'''
import os
path=input('输入安装地址（右键粘贴，或直接回车使用该安装程序所在目录）')+'\\'
if path=='':
    path= os.getcwd()+'\\'
while not os.path.exists(path):
    print('该路径不存在')
    path=input('输入安装地址（右键粘贴，或直接回车使用该安装程序所在目录）')
    if path=='':
        path= os.getcwd()
'''
    part_3=r'''
for i in range(len(file_name)):
    with open(path+file_name[i], 'wb') as f:
        exec('f.write(File_%s)'%i)
'''

    file_name=os.listdir(path)
#将文件列表，并以二进制写入。
    try:
        f=open(topath+exe_name, 'w', encoding="utf-8")
        f.write(part_1)
        f.write(('file_name='+str(file_name)+'\n'))
        for n in range(len(file_name)):
            with open(path+file_name[n], 'rb') as ff:
                f.write(('File_'+str(n)+'='))
                f.write(str(ff.read())+'\n')
        f.write(part_3)
    finally:
        if f:
            f.close()

installpy(r'D:\alangrage\走石子\dist')