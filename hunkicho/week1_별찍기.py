#https://www.acmicpc.net/problem/2438

# 처음 실패
# 이유 -> 반복문 모름
# import sys
# star = ""
# n = int(sys.stdin.readline())

# for i in range(1,n+1):
#     for _ in range(i):
#         star += "*"
#     print(star,end='')
#     print()

# 두번째 정답
# import sys
# n = int(sys.stdin.readline())

# for i in range(n):
#     for _ in range(i + 1):
#         print('*',end='')
#     print()

# 성능개선(다른사람거 봄)
import sys
n = int(sys.stdin.readline())

for i in range(1, n+1):
    print("*" * i)