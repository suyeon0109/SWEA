for tc in range(10):

    # 인덱스 에러 방지하기 위해 양 옆에 [0] 붙인다
    n = int(input())
    la = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]
    cnt_m = 100*100

    for x in range(102):
        cnt = 0
        # 1이면, 사다리 카운트 시작
        if la[0][x] == 1:
            i = 0
            j = x

            # 행 막줄 도달할 때까지 한칸씩 걸으면서 카운트
            while i != 99:
                if la[i][j-1] == 1:
                    while la[i][j-1] == 1:
                        j -= 1
                        cnt += 1
                elif la[i][j+1] == 1:
                    while la[i][j+1] == 1:
                        j += 1
                        cnt += 1
                i += 1
                cnt += 1

            # 카운트 최솟값 지정
            if cnt < cnt_m:
                cnt_m = cnt
                num = x

        else:
            pass

    print(f'#{tc+1}',num-1)