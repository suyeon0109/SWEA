for tc in range(int(input())):
    N = int(input())
    la = [list(map(int, input())) for _ in range(N)]
    s = 0

    for i in range(N//2+1):
        s += sum(la[i][N//2-i : N//2+i+1])
    for j in range(N//2+1,N):
        s += sum(la[j][N//2 - (N-j-1) : N//2 + (N-j)])
    
    print(f'#{tc+1}',s)