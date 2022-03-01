for tc in range(int(input())):
    n,c = map(str, input().split())
    la = list(map(int, n))
    cnt = 0

    for i in range(len(la)-1):
        for j in range(len(la)-1, i, -1):
            if la[j] == max(la[i+1:]) and la[i] < max(la[i+1:]):
                la[i], la[j] = la[j], la[i]
                cnt += 1
        if cnt == int(c):
            break
    
    if int(c) > cnt:
        for _ in range(int(c)-cnt):
            for k in range(len(la)-2, 0, -1):
                if la[k] == min(la[:-1]):
                    la[k],la[-1] = la[-1],la[k]
    
    print(f'#{tc+1}',*la)

    3 2 7 8 8 
    8 2 7 8 3
    8 8 7 2 3 


    3 2 7 8 9
    9 2 7 8 3
    9 8 7 2 3


    3 2 8 8 7
    8 2 8 3 7
    8 8 2 3 7

    3 8 2 6 8
    8 8 2 6 3