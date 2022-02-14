for i in range(int(input())):
    a, b = map(int, input().split())
    la=[list(map(int, input().split())) for _ in range(a)]

    max_s = 0
    for x in range(a-b+1):
        for y in range(a-b+1):
            s = 0
            for k in range(b):
                for l in range(b):
                    s += la[x+k][y+l]
            if s > max_s:
                max_s = s
    
    print(f'#{i+1}',max_s)
