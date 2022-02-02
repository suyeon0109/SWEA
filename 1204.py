for i in range(int(input())):
    num = int(input())
    k = list(map(int, input().split()))
    dict_a = {}

    for j in k:
            dict_a[j]=k.count(j)
    
    print(f'#{i+1}',max(zip(dict(dict_a).values(), dict(dict_a).keys()))[0])
