n = int(input())
sum_flies = 0
list_flies=[]

flies_n,kill_n = map(int, input().split())
for w in range(n):
    for i in range(flies_n):
        list_flies.append(list(map(int, input().split())))

    for k in range(len(list_flies)):
        for m in range(len(list_flies)):
            try:
                s = 0
                for i in range(kill_n):
                    for j in range(kill_n):
                        s += list_flies[i+k][j+m]
                        print(s)
                if sum_flies < s :
                    sum_flies = s
            except:
                pass
    print(f'#{w+1} ', sum_flies)
