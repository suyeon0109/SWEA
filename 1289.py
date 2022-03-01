for tc in range(int(input())):
    cnt = 0
    s = '0'
    la = ['0', '1']
    m = input()

    for i in range(len(m)):
        if m[i] == s:
            pass
        else:
            cnt += 1
            s = list(set(la)-set(s))[0]
        
    print(f'#{tc+1}', cnt)
