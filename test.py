t = int(input())

#total_num_set = set() #지금까지 나온 자리수 담는 셋 (중복 없어야 함) // 셋이든 리스트든 상관없나??
#첫번째 시도 풀이
for i in range(1, t+1):
    n = int(input())
    num_list = [] #* 10 #현재 각 자리수를 담는 리스트

    cnt = 1
    while len(num_list) != 10:
        cnt += 1
        ##cnt=1 여기에 쓰면 while문 돌릴때마다 1로 초기화됨
        number = str(n * cnt) #'29 * 1 = 29
        for j in number:
            if int(j) not in num_list:
                num_list.append(int(j))
            print(num_list)
            print(cnt)
            print(n)

    print(cnt * n)