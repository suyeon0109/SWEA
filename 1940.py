# for i in range(int(input())):
#     s = 0
#     v = 0

#     for j in range(int(input())):
#         com = list(map(int, input().split()))

#         if len(com) == 1:
#             s += v
#         if com[0] == 1:
#             s += v + (1/2) * com[1]
#             v = v + com[1]
#         elif com[0] == 2:
#             s += v - (1/2) * com[1]
#             v = v + com[1]
#     if s<0:
#         s = 0
#     print(f'#{i+1}', s)

for i in range(int(input())):
    s = 0
    v = 0

    for j in range(int(input())):
        com = list(map(int, input().split()))

        if len(com) == 1:
            s += v
        if com[0] == 1:
            s += v + com[1]
            v = v + com[1]
        elif com[0] == 2:
            s += v - com[1]
            v = v - com[1]
    if s<0:
        s = 0

    print(f'#{i+1}',s)
