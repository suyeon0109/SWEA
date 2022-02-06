d1 = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

for i in range(int(input())):
    a, b, c, d = map(int, input().split())
    if a == c:
        print(f'#{i+1}', d-b+1)
    else:
        s = 0

        s += d1[a] - b + 1 + d
        for j in range(a+1,c):
            s += d1[j]
        print(f'#{i+1}', s)
        