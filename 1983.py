T=int(input())

for i in range(T):

    N,K = map(int,input().split())

    # 학생 순으로 번호 메겨서 시험점수와 같이 딕셔너리에 저장
    dict_sum = {}

    for j in range(N):
        mid, final, homework = map(int,input().split())
        dict_sum[j+1] = 35*mid/100 + 45*final/100 + 20*homework/100
    
    # 만들어진 딕셔너리를 value값 기준으로 정렬
    # 정렬 후 key값을 순서대로 새로운 리스트에 추가
    list_sum = []
    d1 = sorted(dict_sum.items(), key = lambda x: x[1])
    for key, value in d1:
        list_sum.append(key)

    # 백분율 s 계산
    s = (list_sum.index(K)+1)/N*100
    
    list_s=['D0','C-','C0','C+','B-','B0','B+','A-','A0','A+']

    if int(str(s)[1]) == 0:                         # 백분율의 1의자리수가 0일때. ex)90,80,,,
        print(f'#{i+1} {list_s[int(str(s)[0])-1]}')
    else:                                           # 백분율 1의자리수가 0이 아닐때. ex)96,85...
        print(f'#{i+1} {list_s[int(str(s)[0])]}')