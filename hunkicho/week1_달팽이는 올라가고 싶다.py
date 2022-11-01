# https://www.acmicpc.net/problem/2869
# import sys

# input_num = list(map(int, sys.stdin.readline().split()))

# num1 = input_num[0] #하루에 올라가는거
# num2 = input_num[1]
# num3 = input_num[2] # 총 길이


# if num1 >= num3:
#     print(num1)
# else:
#     height = num3 - num1
#     if height % (num1-num2) != 0:
#         if height // num1 == 1:
#             print((height // (num1-num2)) + 1)
#         else:
#             check = num3 - (height * (height // num1))

#             print((height // (num1-num2)) + 1)
#     else:
#         print((height // (num1-num2)) + 1)


# 성공
import sys

input_num = list(map(int, sys.stdin.readline().split()))

num1 = input_num[0] #하루에 올라가는거
num2 = input_num[1]
num3 = input_num[2] # 총 길이


if num1 >= num3:
    print(1)
else:
    height = num3 - num1
    if height % (num1-num2) == 0:
        print(height // (num1-num2) + 1)
    else:
        print(height // (num1-num2) + 2)



# 더 간단한거, 처음에 num1 > num3 비교할 필요 없다
import sys

a, b, v = list(map(int, sys.stdin.readline().split()))

print((v - a) // (a - b) + 1 if (v - a) % (a - b) == 0 else (v - a) // (a - b) + 2)