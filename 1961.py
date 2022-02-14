for i in range(int(input())):
    la = []
    n = int(input())
    for j in range(n):
        la.append(list(map(int, input().split())))
    
    print(f'#{i+1}')
    for m in range(n):

        # 741 987 369
        for k in range(len(la)-1,-1,-1):
            print(la[k][m],end='')

        # 852 654 258
        print(' ', end = '')
        print(*reversed(la[-1-m]),sep = '',end =' ')

        # 963 321 147
        for l in range(len(la)):
            print(la[l][-1-m],end = '')
        print()
    