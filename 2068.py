n=int(input())
for i in range(n):
    list_a=list(map(int, input().split()))
    print(f'#{i+1}', max(list_a))