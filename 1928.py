d1={}
for i in range(26):
    d1[i] = chr(65+i)
for i in range(26,52):
    d1[i] = chr(71+i)
for i in range(10):
    d1[52+i] = str(i)

d1[62] = '+'
d1[63] = '/'
l1 = list(d1.items())

m = input()
s = ''
for i in m:
    for key,value in l1:
        if i == value:
            if len(str(bin(key)))<6:
                s += (6-len(str(bin(key))))*'0'+str(bin(key))[2:]
            else:
                s += str(bin(key))[2:]
i = 1
b = ''
print(s)
    



