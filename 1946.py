for i in range(int(input())):
    m = ''
    for _ in range(int(input())):
        a,b = map(str, input().split())
        m += a*int(b)
    
    k = 0
    print(f'#{i+1}')
    while k < len(m):
        print(m[k:k+10])
        k += 10