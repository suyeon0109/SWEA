def qqq(a,b):
    if a>b:
        return '>'
    elif a<b:
        return '<'
    else :
        return '='

n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    print(f'#{i+1}', qqq(a,b))
