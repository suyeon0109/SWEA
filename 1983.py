T=int(input())
for i in range(T):
    N,K=map(int,input().split())
    dict_sum={}
    for j in range(N):
        a,b,c=map(int,input().split())
        dict_sum[i+1]=a+b+c
    d1=sorted(dict_sum.items(), key=lambda x: x[1])
    d1[K]


    s=list_sum.index(dict_sum[K-1])/N*100
    list_s=['D0','C-','C0','C+','B-','B0','B+','A-','A0','A+']
    print(f'#{i+1} {list_s.index(int(str(s)[0]))}')
