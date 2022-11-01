# https://www.acmicpc.net/problem/1152

# import sys

# count = 0
# input_str =  list(map(str, sys.stdin.readline().split()))
# for i in input_str:
#     if i == " ":
#         count += 1
# print(len(input_str) - count)


#split 안에 아무것도 안쓰면 자체가 공백 기준으로 잘라서 저장해서 이렇게 해도 됨
import sys

count = 0
print(len(list(map(str, sys.stdin.readline().split()))))

