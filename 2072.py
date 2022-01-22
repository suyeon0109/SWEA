n=int(input())
for i in range(n):
    s=0
    list_number=list(map(int, input().split()))
    for j in list_number:
        if j%2!=0:
            s+=j
    print(f'#{i+1} {s}')
    