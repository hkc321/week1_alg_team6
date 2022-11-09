# https://www.acmicpc.net/problem/2908

# 인터넷봄
import sys

num_list = list(map(str, sys.stdin.readline().split()))

final_list = []
for i in range(2):
    num = ""
    for j in list(num_list[i]):
        num = j + num
    final_list.append(num)
print(final_list[0]) if final_list[0] > final_list[1] else print(final_list[1])