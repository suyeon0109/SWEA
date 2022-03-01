for tc in range(10):
    n = int(input())
    la = [list(map(int, input().split())) for _ in range(100)]

    # 행안에서 연산하는게 좋아서 전치 시킴
    for i in range(100):
        for j in range(i+1,100):
            la[i][j], la[j][i] = la[j][i], la[i][j]
    
    # 행 안의 0들을 다 지워버린다.
    for p in la:
        while 0 in p:
            p.remove(0)

    cnt = 0

    # 교착상태 -> [1,2]의 갯수로 볼 수 있음
    # 왼쪽이 N극, 오른쪽이 S극 이므로 1,2 로 세야한다!
    for l in la:
        for k in range(len(l)-1):
            if l[k:k+2] == [1,2]:
                cnt += 1

    print(f'#{tc+1}',cnt)