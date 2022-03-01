T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [[3]*N + list(map(int, input().split())) + [3]*N for _ in range(N)]
    # 새로운 최종 리스트 arr로 선언
    arr = [[3]*(3*N)]*N + lst + [[3]*(3*N)]*N
    
    di = [-1, 1, 0, 0]  #상 하 좌 우
    dj = [0, 0, -1, 1]
    # dir = 0
    # num = 2
    for i in range(N, N+N+1):
        for j in range(N, N+N+1):
            if arr[i][j] == 2:
                r = i
                c = j 

    for k in range(4):  #방향탐색
        for h in range(1, N):
            ni = r + di[k]* h
            nj = c + dj[k]* h
            if arr[ni][nj] == 0:
                arr[ni][nj] = 2
            
            # 3이나 1을 만나면, 반복문 종료
            elif arr[ni][nj] == 3 or arr[ni][nj] == 1:
                break

    cnt = 0
    for i in range(3*N):
        for j in range(3*N):
            if arr[i][j] == 0:
                cnt+=1
    print(f'#{tc} {cnt}')