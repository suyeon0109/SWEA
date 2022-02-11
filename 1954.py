import copy

for i in range(int(input())):
    N = int(input())
    la = [[0]* N]
    lb = []
    for n in range(N):
        lb += copy.deepcopy(la)

    x,y = 0,-1
    cnt = 0
    j = 0

    while N != 0:

        for k in range(1,N+1):
            cnt +=1
            y += (-1)**j
            lb[x][y] = cnt

        for m in range(1,N):
            cnt += 1
            x += (-1)**j
            lb[x][y] = cnt

        j += 1
        N -= 1

    print(f'#{i+1}')
    for p in range(len(lb)):
        print(*lb[p])
    