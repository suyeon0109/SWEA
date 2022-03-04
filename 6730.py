for tc in range(int(input())):
    n = int(input())
    la = list(map(int, input().split()))
    up = [0]
    down = [0]

    for i in range(len(la)-1):
        if la[i+1]-la[i] < 0:
            down.append(la[i+1]-la[i])
        else:
            up.append(la[i+1]-la[i])
    print(f'#{tc+1}',max(up),abs(min(down)))