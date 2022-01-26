for i in range(int(input())):
    k = list(map(int, input().split()))
    dict_a = {}

    for i in k:
        dict_a.setdefault(i,k.count(i))
    
    print(max(dict_a))
