import os
import random
def raname(mainpath):
    files=os.listdir(mainpath)
    types=[]
    names_o=[]
    for i in files:
        types.append(i[i.rfind('.'):])
        names_o.append(i[:i.rfind('.')])
    for i in range(len(files)):
        c=1
        while c:
            x=str(random.randint(100000,999999))
            if x not in names_o:
                os.rename(mainpath+'\\'+files[i],mainpath+'\\'+x+types[i])
                names_o.append(x)
                c=0
        


raname(r'D:\aaa\wallpaperpicture')
