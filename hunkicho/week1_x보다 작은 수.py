#https://www.acmicpc.net/problem/10871

# 처음 실패
# import sys

# count,comparison = map(int, input().split())
# num_list = [int(sys.stdin.readline()) for _ in range(count-1)]

# for i in num_list:
#     if i < 5:
#         print(i, end=' ')


#두번쨰 성공 (다른사람거)
# import sys

# count,comparison = map(int, input().split())
# num_list = list(map(int, sys.stdin.readline().split()))

# for i in range(count):
#     if num_list[i] < comparison:
#         print(num_list[i], end=' ')


#성능개선(다른사람거)
import sys

N, X = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
output =[]
for i in range(N):
    if A[i] < X:
        output.append(A[i])
    else:
        pass
output = [str(i) for i in output]
print(' '.join(output))