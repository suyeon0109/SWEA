T = int(input())
for test in range(T):

    N = int(input())
    list_i = [2,3,5,7,11]
    list_n = []
    for i in list_i:

        cnt = 0
        while N%i == 0:
            cnt += 1
            N = N//i

        list_n.append(str(cnt))

    a = ' '.join(list_n)


    print(f'#{test+1} {a}')