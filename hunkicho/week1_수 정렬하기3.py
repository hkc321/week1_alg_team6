# https://www.acmicpc.net/problem/2751

# import sys

# def fsort(a, max):
#     n = len(a) # 정렬할 배열 a
#     f = [0] * (max+1) # 도수 분포표
#     b = [0] * n # 작업용

#     for i in range(n):
#         f[a[i]] += 1
#     for i in range (1,max+1):
#         f[i] += f[i-1]
#     for i in range (n-1,-1,-1):
#         f[a[i]] -= 1
#         b[f[a[i]]] = a[i] = a[i]
#     for i in range(n):
#         a[i] = b[i]
#     b = []
#     for i in a:
#         print(i)

# def count_sort(a) -> None:
#     #도수 정렬
#     fsort(a,max(a))

# count = int(sys.stdin.readline())
# num = [0] * count

# for i in range(count):
#     num[i] = int(sys.stdin.readline())

# count_sort(num)



# https://leunco.tistory.com/67
# 배열의 인데스를 특정한 데이터의 값으로 여기는 방법
# 배열의 크기는 데이터의 범위를 포함할 수 있도록 설정
# 데이터가 등장한 횟수를 셈
import sys

n = int(sys.stdin.readline())
array = [0] * 10001

for i in range(n):
    data = int(sys.stdin.readline())
    array[data] += 1

for i in range(10001):
    if array[i] != 0:
        for j in range(array[i]):
            print(i)