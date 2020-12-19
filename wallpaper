import os
import win32api
from time import sleep
from shutil import copy
from shutil import rmtree
def image_move(old_path,new_path):
    n_o_p = os.listdir(old_path)
    nop_len = len(n_o_p)
    for l in range(0,nop_len):
        if n_o_p[l].endswith('.jpg'):
            copy(old_path+'\\'+n_o_p[l],new_path)
        elif n_o_p[l].endswith('.png'):
            copy(old_path+'\\'+n_o_p[l],new_path)
        elif n_o_p[l].endswith('.JPG'):
            copy(old_path+'\\'+n_o_p[l],new_path)
        else:
            pass
steam_path = r'D:\SteamLibrary\steamapps\workshop\content\431960\\'
mainpath = os.getcwd()#获取基本信息
download_listmain = os.listdir(steam_path)
f_len = len(download_listmain)
print('wallpaper engine 下载的文件总数为'+ str(f_len))#输出文件个数
valid_file =[]
for i in range(0,f_len):
    name_son = download_listmain[i]
    d_list_s = os.listdir(steam_path+ name_son)
    if 'scene.pkg'in d_list_s:
        valid_file.append(name_son)
valid_f_len = len(valid_file)
print('可提取的文件数量为'+ str(valid_f_len))
for o in range(0,valid_f_len):
    new_name = str(o)
    old_f_n = valid_file[o]
    copy(steam_path+old_f_n+'\scene.pkg',mainpath+'\scene.pkg')
    os.rename(mainpath+'\scene.pkg',mainpath+'\\'+str(o)+'.pkg')
a = 6.5 + valid_f_len*1.5
print('解压预计需要'+str(a)+'秒')
win32api.ShellExecute(0, 'open', mainpath + r'\pkg.exe','','',0)
sleep(a)
print('解压完成,结束解压程序')
os.system('taskkill /f /t /im '+'pkg.exe')#结束解压程序
for k in range(0,valid_f_len):
    n_old_file = mainpath + '\\' + str(k) + '-解包\\materials'
    image_move(n_old_file,mainpath + '\\成品')
print('清理冗余文件')
for u in range(0,valid_f_len):
    os.remove(mainpath+'\\'+str(u)+'.pkg')
    rmtree(mainpath + '\\' + str(u) + '-解包')
print('程序结束')
