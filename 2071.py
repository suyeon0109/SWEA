import math
n=int(input())
for i in range(n):
    list_a=list(map(int, input().split()))
    print(f'#{i+1}',round(sum(list_a)/len(list_a)))