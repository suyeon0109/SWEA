for i in range(int(input())):
    p = int(input())
    loc = list(map(int, input().split()))
    dict_l = {}
    for j in loc:
        dict_l[j] = abs(j)
    
    a = min(zip(dict(dict_l).values(), dict(dict_l).keys()))[0]
    count = 0
    for k in dict_l:
        if dict_l[k]==a:
            count += 1
    print(f'#{i+1}',a,count)
