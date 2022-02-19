for tc in range(int(input())):
    n = int(input())
    la = [list(map(int, input().split())) + [0] for _ in range(n)]
    lb = []
    lc = {}
    
    for i in la:
        cnt = 0
        for j in range(len(i)):
            if i[j] != 0:
                cnt += 1
            else:
                if cnt == 0:
                    pass
                else:
                    lb.append(cnt)
                    cnt = 0

    for i in list(set(lb)):
        lc[(lb.count(i), i)] = lb.count(i)*i

    ld = list(sorted(zip(lc.values(),lc.keys())))

    print(f'#{tc+1}',len(set(lb)),end=' ')
    for i in ld:
        print(i[1][0], i[1][1], end=' ')
    print()