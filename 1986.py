for j in range(int(input())):
    N = int(input())
    sum = 0
    for i in range(1,N+1):
        sum += i*((-1)**(i+1))
    print(f'#{j+1}',sum)