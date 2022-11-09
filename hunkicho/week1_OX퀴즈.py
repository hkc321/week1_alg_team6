#https://www.acmicpc.net/problem/8958

#출력초과?
# import sys
# count = int(sys.stdin.readline())


# for _ in range(count):
#     ox_list = list(sys.stdin.readline())
#     n=0
#     sum_list = []
#     for i in ox_list:
#         print(i)
#         if i == 'O':
#             n += 1
#             sum_list.append(n)

#         elif i == 'X':
#             n = 0
#     print(sum(sum_list))

import sys
count = int(sys.stdin.readline())

for _ in range(count):
    ox_list = list(sys.stdin.readline())
    n = 0
    sum_list = []
    for i in ox_list:
        if i == 'O':
            n += 1
            sum_list.append(n)

        elif i == 'X':
            n = 0
    print(sum(sum_list))