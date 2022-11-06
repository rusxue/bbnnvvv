import os

mainpath = r'C:\Users\xue\Documents\Klei\OxygenNotIncluded\mods\Local'#os.getcwd()
mdir=os.listdir(mainpath)
for i in mdir:
    print (i)
    path1=os.listdir(mainpath+'\\'+i)
    for x in path1:
        if '.dll' in x:
            os.rename(mainpath+'\\'+i,mainpath+'\\'+x[:-4])
            break
