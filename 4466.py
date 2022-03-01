for tc in range(int(input())):
    N,K = map(int, input().split())
    score = list(map(int, input().split()))
    s = 0

    for i in range(K):
        # 최고점을 max를 이용해 s에 더함
        # 더하고 나면 지워버린다. -> 제거된 리스트에서 다시 max값 찾기!
        s += max(score)
        score.remove(max(score))
    
    print(f'#{tc+1}',s)