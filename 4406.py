for tc in range(int(input())):
    m = input()
    la = ['a', 'e', 'i', 'o', 'u']
    for i in la:
        m = m.replace(i,'')
    print(f'#{tc+1}',m)