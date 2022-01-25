n = int(input())
for i in range(n):
    list_p = {}
    for j in range(1, int(input())):
        if j == 1:
            list_p[j]=1
        for k in range(j):
            if j == 2:
                list_p[j][k] = 1
            else:
                try :
                    list_p[j][k] = list_p[j-1][k-1]+list_p[j-1][k]
                except:
                    list_p[j][k] = 1
        print(list_p[j])