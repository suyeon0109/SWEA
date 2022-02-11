for i in range(int(input())):
    N, K = map(int, input().split())
    la = []
    for j in range(N):
        la.append(list(map(int, input().split())))
    
    # 가로
    cnt = 0
    for k in la:
        for m in range(N-K+1):
            if k[m] == k[m+1] == k[m+2] == 1:
                if m-1 <0:
                    try:
                        if k[m+3] == 0:
                            cnt += 1
                    except:
                        cnt += 1
                else:
                    if k[m-1] == 0:
                        try:
                            if k[m+3] == 0:
                                cnt += 1
                        except:
                            cnt += 1
    

    
    for
    print(cnt)
