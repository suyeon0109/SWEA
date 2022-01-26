def split_p(string):
    return list(map(int, string.split(' ')))

def pascal(n):
    if n == 1:
        return '1'
    elif n == 2:
        return '1 1'
    else:
        s = '1 '
        for i in range(1, n-1):
            s += str(split_p(pascal(n-1))[i-1] + split_p(pascal(n-1))[i])
            s += ' '
        s += '1'
        return s

for case in range(int(input())):
    print(f'#{case+1}')
    for size in range(int(input())):
        print(pascal(size+1))

        