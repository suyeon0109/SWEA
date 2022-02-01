for i in range(int(input())):

    list_N=[]
    N = int(input())
    list_N.extend(str(N))
    cnt = 1

    while len(set(list_N))!=10:
        list_N.extend(str(N * (cnt+1)))
        cnt += 1
       
    
    print(f'#{i+1}',N*cnt)
