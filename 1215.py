for tc in range(10):
    n = int(input())
    la = [list(map(str, input())) for _ in range(8)]

    cnt = 0
    for i in la:
        for j in range(8-n+1):
            if i[j:j+n] == i[j:j+n][::-1]:
                cnt += 1
    
    for k in range(8):
        for l in range(k+1,8):
            la[k][l], la[l][k] = la[l][k], la[k][l]
    
    for p in la:
        for q in range(8-n+1):
            if p[q:q+n] == p[q:q+n][::-1]:
                cnt += 1

    print(f'#{tc+1}', cnt)