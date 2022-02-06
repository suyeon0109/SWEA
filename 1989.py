for i in range(int(input())):
    a = input()
    s = ''
    for j in range(-1,-len(a)-1, -1):
        s += a[j]

    if s == a:
        print(f'#{i+1}',1)
    else:
        print(f'#{i+1}',0)
