import os
import zipfile

pic=input('图片目录')
zip1=input('文件目录')
type_pic=input('输入后缀')
newZip = zipfile.ZipFile('.zip','w')
newZip.write(zip1, compress_type=zipfile.ZIP_DEFLATED)
newZip.close()
os.system('copy /b '+pic+'+'+zip1+'.zip'+' '+zip1+'.'+type_pic)

