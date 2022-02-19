# 이익 함수 생성.
def revenue(b):
    b_n = b[:b.index(max(b))+1]
    a = b_n[-1]*(len(b_n)-1)-sum(b_n[:-1])
    del b[:b.index(max(b))+1]
    return a
    
'''
함수 설명: 주어진 리스트(b)의 맥스값이 있으면,
첫 인덱스부터 맥스값 까지의 요소를 가지는 새로운 리스트(b_n) 생성 후,
b_n의 인덱스를 활용하여 이익(a) 계산.
그 다음 b_n의 요소를 기존 리스트 b에서 삭제한다.
'''

# 테스트 케이스 입력
n=int(input())

# 테스트 케이스 갯수동안 루프
for i in range(n):

    # 매매가 개수(m) 입력
    m = int(input())

    # 매매가 리스트(b) 입력, 이익을 더할 빈 리스트(r) 생성
    b = list(map(int,input().split()))
    r = []

    # 함수 호출. 리스트 b가 []가 될때 까지 함수를 반복하게 되면
    # 이익 a들이 빈 리스트 r에 추가된다.
    while b == True:
        r.append(revenue(b))
    
    # 리스트 r에 추가된 이익들을 합하면 총 이익이 계산.
    print(f'#{i+1}',sum(r))

