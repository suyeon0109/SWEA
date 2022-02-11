for i in range(int(input())):
    n = int(input())
    la = list(map(int, input().split()))
    for k in range(len(la)):
        for j in range(len(la) - 1):
            if la[j] > la[j+1]:
                la[j], la[j+1] = la[j+1], la[j]
            else:
                pass

    print(f'#{i+1}', *la)