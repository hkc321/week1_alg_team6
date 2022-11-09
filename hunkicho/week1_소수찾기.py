# https://www.acmicpc.net/problem/1978


# 틀린 코드
# 리스트에서 1인 요소 지우고 input_count -1 안함

# import sys
# import math

# input_count = int(sys.stdin.readline())
# input_num = list(map(int, sys.stdin.readline().split()))

# if input_num.count(1) > 0:
#     input_num.remove(1)

# for i in input_num:
#     for j in range (2, int(math.sqrt(i)) + 1):
#         if i % j == 0:
#             input_count -= 1
# print(input_count)




# 에라토스테네스의 체 이용
# 약수의 성질: 모든 약수는 가운데 약수를 기준으로 곱셈 연산에 대해 대칭을 이룬다.
# 따라서 특정 자연수의 모든 약수를 찾을 떄 가운데 약수(제곱근) 까지만 확인하면 된다.
# 8이 2로 나누어 떨어지면 4로도 나누어 떨어진다.
# 소수 판단할 때도 1과 자기 자신 사이까지 다 할 필요없고 2부터 제곱근 까지만 하면 된다.

import sys
import math

input_count = int(sys.stdin.readline())
input_num = list(map(int, sys.stdin.readline().split()))

if input_num.count(1) > 0:
    input_num.remove(1)
    input_count -= 1

for i in input_num:
    for j in range (2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            input_count -= 1
            break
print(input_count)