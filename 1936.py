dict_rsp={1:0, 2:0, 3:0}
A,B=map(int, input().split())
dict_rsp[A]='A'
dict_rsp[B]='B'
if dict_rsp[1]!=0 and dict_rsp[2]!=0 :
    print('{}'.format(dict_rsp[2]))
elif dict_rsp[2]!=0 and dict_rsp[3]!=0:
    print('{}'.format(dict_rsp[3]))
elif dict_rsp[1]!=0 and dict_rsp[3]!=0:
    print('{}'.format(dict_rsp[1]))
else:
    print('Draw')