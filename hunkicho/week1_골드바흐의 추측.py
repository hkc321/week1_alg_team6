# https://www.acmicpc.net/problem/9020

# 배열 초기화 안함
# import sys
# import math

# print_list = []
# check_num = []
# count = int(sys.stdin.readline())

# for i in range(count):
#     input_num = int(sys.stdin.readline())
#     num_list = []
#     for j in range(2, input_num + 1):
#         is_yn = "Y"
#         for k in range(2, int(math.sqrt(j)) + 1):
#             if j % k == 0:
#                 is_yn = "N"
#                 break
#         if is_yn == "Y":
#             num_list.append(j)
#     num_list.pop()
#     #print(num_list)
#     if num_list.count(j / 2) > 0:
#         print_list.append((int(j/2),int(j/2)))
#     else:
        
#         for y in num_list:
#             if num_list.count(j-y) > 0:
#                 check_num.append((y,j-y))

#         print(check_num)
#         #print(len(check_num))
#         gap = abs(check_num[0][0] - check_num[0][1])
#         last = check_num[0]
#         for k in check_num[1:len(check_num)-1]:
#             if abs(k[0]-k[1]) < gap:
#                 gap = k[0]-k[1]
#                 last = k
#         print("last=",last)
#         print_list.append(last)
#         #print_list.append((num_list[int((len(num_list)) / 2) - 1],num_list[int((len(num_list)) / 2)]))

# for (first,second) in print_list:
#     print(first,second)


# 시간초과
# import sys
# import math

# print_list = []
# count = int(sys.stdin.readline())

# for i in range(count):
#     input_num = int(sys.stdin.readline())
#     num_list = []
#     for j in range(2, input_num + 1):
#         is_yn = "Y"
#         for k in range(2, int(math.sqrt(j)) + 1):
#             if j % k == 0:
#                 is_yn = "N"
#                 break
#         if is_yn == "Y":
#             num_list.append(j)
#     num_list.pop()
#     ##### 입력한 수의 소수 담기 ####
#     if num_list.count(j / 2) > 0:
#         print_list.append((int(j/2),int(j/2)))
#     else:
#         check_num = []
#         #print("num_list",num_list)
#         for y in num_list:
#             if num_list.count(abs(j-y)) > 0:
#                 check_num.append((y,j-y))
#                 num_list.remove(abs(j-y))
#         gap = abs(check_num[0][0] - check_num[0][1])
#         last = check_num[0]
#         for k in check_num[1:len(check_num)-1]:
#             if abs(k[0]-k[1]) < gap:
#                 gap = k[0]-k[1]
#                 last = k
#         print_list.append(last)

# for (first,second) in print_list:
#     print(first,second)




import sys
import math

print_list = []
count = int(sys.stdin.readline())

for i in range(count):
    input_num = int(sys.stdin.readline())
    num_list = []
    for j in range(2, input_num + 1):
        is_yn = "Y"
        ##### 입력한 수의 소수 담기 ####
        for k in range(2, int(math.sqrt(j)) + 1):
            if j % k == 0:
                is_yn = "N"
                break
        if is_yn == "Y":
            num_list.append(j)
    num_list.pop()

    
    check_num = []
    for y in num_list:
        if num_list.count(abs(j-y)) > 0:
            check_num.append((y,j-y))
            num_list.remove(abs(j-y))
    gap = abs(check_num[0][0] - check_num[0][1])
    last = check_num[0]
    for k in check_num[1:len(check_num)-1]:
        if abs(k[0]-k[1]) < gap:
            gap = abs(k[0]-k[1])
            last = k
    print_list.append(last)

for (first,second) in print_list:
    print(first,second)
