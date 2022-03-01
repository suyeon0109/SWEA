for tc in range(int(input())):
    n = int(input())
    la = [list(map(int, input().split())) + [0] for _ in range(n)]
    lb = []
    lc = {}
    
    for i in la:
        cnt = 0
        for j in range(len(i)):

            # 0이 아닌 수의 갯수를 세면, 상자의 열 길이가 나온다.
            # 열길이의 총 갯수는 행길이가 된다. 
            if i[j] != 0:
                cnt += 1
            else:
                # 요소가 0일때, 그 전까지의 카운트가 0이었으면 그냥 패스하고,
                # 카운트가 0이 아니었으면 그때까지 셌던 카운트를 저장한다.-> 상자 길이 저장
                if cnt == 0:
                    pass
                else:
                    lb.append(cnt)
                    cnt = 0

    # 딕셔너리를 만든다. {(행길이, 열길이) : 상자 넓이,,,,,,}
    for i in list(set(lb)):
        lc[(lb.count(i), i)] = lb.count(i)*i

    # 출력을 상자 넓이 순으로 해야하기 때문에, 딕셔너리를 value값 기준으로 정렬시킨다. (오름차순)
    ld = list(sorted(zip(lc.values(),lc.keys())))

    # 이제 출력~
    print(f'#{tc+1}',len(set(lb)),end=' ')
    for i in ld:
        print(i[1][0], i[1][1], end=' ')
    print()