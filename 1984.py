n = int(input())

for i in range(n):

    list_n = list(map(int, input().split()))

    list_n.remove(max(list_n))
    list_n.remove(min(list_n))
    
    print(f'#{i+1}',round(sum(list_n)/8))
