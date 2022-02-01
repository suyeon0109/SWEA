for i in range(int(input())):
    p,q,r,s,w = map(int, input().split())

    A = w * p
    if w <= r:
        B = q
    else:
        B = q + (w-r)*s

    if A<B:
        print(f'#{i+1}',A)
    else:
        print(f'#{i+1}',B)