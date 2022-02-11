
for tc in range(int(input())):
    sudoku=[]
    for _ in range(9):
        sudoku.append(list(map(int, input().split())))
        
#------------------스도쿠 완성------------------#

    cnt = 0
    
    # 가로줄 체크
    for w in sudoku:
        check = [0,0,0,0,0,0,0,0,0]
        for e in range(9):
            check[w[e]-1] += 1

        if 0 in check:
            cnt += 1
            break
    
    # 세로줄 체크
    for e in range(9):
        check = [0,0,0,0,0,0,0,0,0]
        for w in sudoku:
            check[w[e]-1] += 1

        if 0 in check:
            cnt += 1
            break

    # 정사각형 체크
    q = 0
    for _ in range(3):
        p = 0
        for _ in range(3):
            check = [0,0,0,0,0,0,0,0,0]
            for l in range(p,p+3):
                for k in range(q, q+3):
                    check[sudoku[k][l]-1] += 1

            if 0 in check:
                cnt += 1
                break
            p += 3
        q += 3

    if cnt == 0:
        print(f'#{tc+1}',1)
    else:
        print(f'#{tc+1}',0)