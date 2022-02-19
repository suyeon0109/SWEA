for tc in range(10):
    n = int(input())
    la = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]
    cnt_m = 100*100

    for x in range(102):
        cnt = 0

        if la[0][x] == 1:
            i = 0
            j = x

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

            if cnt < cnt_m:
                cnt_m = cnt
                num = x

        else:
            pass

    print(f'#{tc+1}',num-1)