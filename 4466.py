for tc in range(int(input())):
    N,K = map(int, input().split())
    score = list(map(int, input().split()))
    s = 0
    for i in range(K):
        s += max(score)
        score.remove(max(score))
    
    print(f'#{tc+1}',s)