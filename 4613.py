for tc in range(int(input())):
    N, M = map(int, input().split())
    la = [input() for _ in range(N)]
    cnt = 0

    for i in la[0]:
        if i != 'W':
            cnt += 1
    for j in la[-1]:
        if j != 'R':
            cnt += 1

    cnt_m = M*N

    for k in range(N-2):

        cnt_n = cnt
        
        for m in la[1:1+k]:

            for n in m:
                if n != 'W':
                    cnt_n += 1
        
        for t in range(N-k-2):

            cnt_t = cnt_n

            for p in la[1+k:1+k+t+1]:
                for w in p:
                    if w != 'B':
                        cnt_t += 1

            for q in la[1+k+t+1:-1]:
                for r in q:
                    if r != 'R':
                        cnt_t += 1

            if cnt_t < cnt_m:
                cnt_m = cnt_t
    
    print(f'#{tc+1}',cnt_m)