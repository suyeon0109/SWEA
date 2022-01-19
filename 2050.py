a='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
dict_1={}
c=1
for i in a:
    dict_1[i]=c
    c+=1

m=input()
for i in m:
    print(dict_1[i], end=' ')