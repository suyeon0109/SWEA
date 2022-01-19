n=int(input())
list_m=list(map(int, input().split()))
list_m.sort()
print(list_m[int((len(list_m)-1)/2)])