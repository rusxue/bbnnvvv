
def txtjiont(txt1,txt2,ftxt=1,ttxt=1):
    if ftxt:
        with open(txt1,'r',encoding='UTF-8') as t1:
            str1=t1.read()
        with open(txt2,'r',encoding='UTF-8') as t2:
            str2=t2.read()
    else:
        str1,str2=txt1,txt2
    s=str1.find(str2[:16])
    print(s)
    print()
txtjiont(r'D:\alangrage\小工具集\notepad\04.txt',r'D:\alangrage\小工具集\notepad\05.txt')

