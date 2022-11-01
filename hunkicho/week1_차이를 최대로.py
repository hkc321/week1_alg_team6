# https://www.acmicpc.net/problem/10819
# https://yangnyang.tistory.com/14
# 순열 이용

# import sys

# input = []

# checksum  = 0
# result_sum = 0

# def perm(arr,n) -> None:
#     result = []
#     if n > len(arr):
#         return result

#     if n == 1:
#         for i in arr:
#             result.append([i])
#     elif n > 1:
#         for i in range(len(arr)):
#             ans = [i for i in arr]
#             ans.remove(arr[i])
#             for p in perm(ans, n-1):
#                 result.append([arr[i]] + p)

#     return result


# c = int(sys.stdin.readline())
    

# input =  list(map(int, sys.stdin.readline().split()))

# final = perm(input,c)

# for i in final:
#     for_resulr = []
#     checksum = 0
#     for j in range(0,len(i) - 1):
#         checksum += abs(i[j] - i[j+1])
#     if checksum > result_sum: 
#         result_sum = checksum

# print(result_sum)


# 재귀함수 이용
import sys

input = []

checksum  = 0
result_sum = 0

def perm(arr,n) -> None:
    result = []
    if n > len(arr):
        return result

    if n == 1:
        for i in arr:
            result.append([i])
    elif n > 1:
        for i in range(len(arr)):
            ans = [i for i in arr]
            ans.remove(arr[i])
            for p in perm(ans, n-1):
                result.append([arr[i]] + p)

    return result


def sum_fac(n,arr):
    if n < c - 1:
        return abs(arr[n] - arr[n+1]) + sum_fac(n+1,arr)
    else:
        return 0


c = int(sys.stdin.readline())
input =  list(map(int, sys.stdin.readline().split()))

final = perm(input,c)

for i in final:
    checksum = sum_fac(0,i)
    if checksum > result_sum: 
        result_sum = checksum

print(result_sum)