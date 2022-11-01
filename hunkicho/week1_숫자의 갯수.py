#https://www.acmicpc.net/problem/2577
import sys

input1 = int(sys.stdin.readline())
input2 = int(sys.stdin.readline())
input3 = int(sys.stdin.readline())

# sum = list(str(input1*input2*input3))
# zero_count = 0
# for i in sum:
#     if i == "0":
#         zero_count += 1
#위에걸 파이썬 내장함수로 간단히 해결 가능
sum_list = list(str(input1*input2*input3))
print(sum_list.count("0"))
print(sum_list.count("1"))
print(sum_list.count("2"))
print(sum_list.count("3"))
print(sum_list.count("4"))
print(sum_list.count("5"))
print(sum_list.count("6"))
print(sum_list.count("7"))
print(sum_list.count("8"))
print(sum_list.count("9"))