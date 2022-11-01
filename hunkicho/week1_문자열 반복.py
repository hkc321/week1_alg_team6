# https://www.acmicpc.net/problem/2675
# 실패-> 마지막 줄바꿈 안함

#import sys

# input = int(sys.stdin.readline())
# for _ in range(input):
#     result = list(map(str, sys.stdin.readline().split()))

#     for i in result[1:]:
#         print(i * int(result[0]),end="")


# 입력을 이상하게 여러번 받음
# import sys

# input = int(sys.stdin.readline())
# for _ in range(input):
#     count = list(map(str, sys.stdin.readline().split()))[0]
#     print(count)
#     result = list(map(str, sys.stdin.readline().split()))[1].split()
#     print(result)


    # for i in result:
    #     print(i * int(count),end="")
    # print()

# import sys

# input = int(sys.stdin.readline())
# for _ in range(input):
#     input = list(map(str, sys.stdin.readline().split()))
#     count = int(input[0])
#     str = input[1].split()
#     for i in str:
#         print(i * count,end="")
#     print()

#내가 문제를 이해 못하나?
import sys

input = int(sys.stdin.readline())

for _ in range(input):
    print_list = []
    print_str = ""
    input_list = list(map(str, sys.stdin.readline().split()))
    count = int(input_list[0])
    str_list = list(input_list[1])
    for i in str_list:
        print_list.append(i * count)
    for i in print_list:
        print_str += str(i)
    print(print_str)
