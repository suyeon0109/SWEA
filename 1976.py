for i in range(int(input())):
    a,b,c,d = map(int, input().split())
    f = (b+d)%60
    e = (a+c+(b+d)//60)%12

    if e == 0:
        e = 12
    print(f'#{i+1}',e,f)