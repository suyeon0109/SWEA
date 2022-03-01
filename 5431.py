for tc in range(int(input())):
    N, K = map(int, input().split())
    la = list(map(int, input().split()))
    lb = []

    for i in range(1,N+1):
        # 리스트 la에 없는 번호를 lb에 추가
        if i not in la:
            lb.append(i)
        
    print(f'#{tc+1}',*lb)