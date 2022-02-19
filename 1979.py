for tc in range(int(input())):
    N, K = map(int, input().split())
    la = [[0] * (N+2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (N+2)]
    cnt = 0
    # 가로
    for i in range(1,N+1):
        for j in range(1,N-K+2):
            if 0 not in la[i][j:j+K] and la[i][j+K] == 0 and la[i][j-1] == 0:
                cnt += 1
    
    # 세로
    for c in range(1,N+1):
        lb = [la[r][c] for r in range(N+2)]
        for p in range(1,N-K+2):
            if 0 not in lb[p:p+K] and lb[p+K] == 0 and lb[p-1] == 0:
                cnt += 1


    print(f'#{tc+1}', cnt)