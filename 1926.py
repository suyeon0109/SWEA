n=int(input())
list_369=['3', '6', '9']

for i in range(n):
    if '3' in str(i+1) or '6' in str(i+1) or '9' in str(i+1):
        count = 0
        for k in str(i+1):
            if k in list_369:
                count +=1
        print('-'*count, end=' ')
    else:
        print(i+1, end=' ')
    
