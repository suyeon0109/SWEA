n = int(input())

for i in range(n):

    string = input()

    for j in range(1,len(string)):
        
        if string[0 : j] == string[j+1 : 2*j+1]:
            print(f'#{i+1}',j+1)
            break
