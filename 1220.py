for tc in range(10):
    n = int(input())
    la = [list(map(int, input().split())) for _ in range(100)]

    for i in range(100):
        for j in range(i+1,100):
            la[i][j], la[j][i] = la[j][i], la[i][j]
    
    for p in la:
        while 0 in p:
            p.remove(0)

    cnt = 0

    for l in la:
        for k in range(len(l)-1):
            if l[k:k+2] == [1,2]:
                cnt += 1

    print(f'#{tc+1}',cnt)