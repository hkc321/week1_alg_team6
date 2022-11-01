#https://www.acmicpc.net/problem/10950

# 처음 실패
# 이유 -> range에 하드코딩
# count = int(input())
# case = []
# for i in range(1,6):
#     a,b = map(int, input().split())
#     case.append(a + b)

# for i in case:
#     print(i)

# 두번째 성공
# count = int(input())
# case = []
# for i in range(1,count+1):
#     a,b = map(int, input().split())
#     case.append(a + b)

# for i in case:
#     print(i)

#성능개선(다른사람거 봄)
import sys
n = int(sys.stdin.readline())
for _ in range(n):
    print(sum(map(int, sys.stdin.readline().split())))