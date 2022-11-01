#https://www.acmicpc.net/problem/2562

# 내가 한거
# import sys

# comp = int(sys.stdin.readline())
# idx = 1

# for i in range(8):
#     input = int(sys.stdin.readline())
#     if input > comp:
#         comp = input
#         idx = i+2

# print(comp,idx,end='\n')


# 성능개선(남이 한거)
# 리스트에 담아서 max함수
import sys
num_list = []

for i in range(1,9+1):
    num_list.append(int(sys.stdin.readline()))

print(max(num_list))
print(num_list.index(max(num_list))+1)