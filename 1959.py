for i in range(int(input())):
    N, M = map(int, input().split())
    lN = list(map(int, input().split()))
    lM = list(map(int, input().split()))

    if len(lN)>len(lM):
        lN, lM = lM, lN
    
    max_s = 0
    for k in range(len(lM)-len(lN)+1):
        s = 0
        for j in range(len(lN)):
            s += lN[j] * lM[k+j]
        if max_s < s:
            max_s = s
    
    print(f'#{i+1}',max_s)
