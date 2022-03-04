for tc in range(int(input())):
    a,b,c = map(int, input().split())
    print(f'#{tc+1}', end = ' ')
    if c < a:
        print(a-c)
    elif c > b:
        print(-1)
    else:
        print(0)