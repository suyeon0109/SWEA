for i in range(int(input())):
    la = []
    n = int(input())
    for j in range(n):
        la.append(list(map(int, input().split())))
    
    print(f'#{i+1}')
    for m in range(n):
        for k in range(len(la)-1,-1,-1):
            print(la[k][m],end='')

        print(' ', end = '')
        print(*reversed(la[-1-m]),sep = '',end =' ')

        for l in range(len(la)):
            print(la[l][-1-m],end = '')
        print()
    