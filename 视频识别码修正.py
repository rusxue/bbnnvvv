import os

def vchange(file_path,add='#7##'):
    ad=str(add)
    with open(file_path,'a') as file:
        file.write(ad)

def blfile(mainpath=os.getcwd()):
    mp4=os.listdir(mainpath)
    for x in mp4:
        if '.mp4' in x:
            vchange(mainpath+'\\'+x)
            print(x)


blfile(r'D:\迅雷下载\FXX\SM')