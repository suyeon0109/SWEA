n = int(input())
for i in range(n):
    m = input()
    for j in range(1,len(m)):
        if m[0 : j] == m[j+1 : 2*j+1]:
            print(f'#{i+1}',j+1)
            break
