 # https://www.acmicpc.net/problem/2309

 # 운빨 알고리즘
# import sys
# import random

# input = [0] * 9
# final = [0] * 9
# for i in range(9): 
#     input[i] =  int(sys.stdin.readline())
# while True:
#     sam = random.sample(input,5)
    
#     if sum(sam) == 100:
#         sam.sort()
#         for i in sam:
#             print(i)
#         break


# https://yangnyang.tistory.com/14
# 순열 이용
import sys

input = []

def combo(arr,n) -> None:
    result = []
    if n > len(arr):
        return result
    if n == 1:
        for i in arr:
            result.append([i])
    elif n > 1:
        for i in range(len(arr) - n + 1):
            for j in combo(arr[i + 1:], n-1):
                result.append([arr[i]] + j)
    return result

def qsort(num,left,right) -> None:
    l = left
    r = right
    middle = num[(l+r) // 2] # 체크값

    while l <= r: #교차 안했으면
        while num[l] < middle : l += 1 #체크값보다 작으면 오른쪽으로
        while num[r] > middle : r -= 1 #체크값보다 크면 왼쪽으로
        if l <= r:  # 커서들이 아직 교차 안했으면 
            num[l],num[r] = num[r],num[l] # 둘이 값을 변경
            l += 1 #커서 증가
            r -= 1 #커서 감소
    if left < r : qsort(num,left,r) #한번 교차했을 떄 오른쪽 커서가 왼쪽 끝에 도착 못했으면
    if l < right : qsort(num,l,right)  #한번 교차했을 떄 왼쪽 커서가 오른쪽 끝에 도착 못했으면

def quick_sort(num) -> None:
    # 리스트 전달하면 왼쪽 커서랑 오른쪽 커서 까지 같이 전달
    qsort(num,0,len(num)-1)
    
for _ in range(9): 
    input.append(int(sys.stdin.readline()))

final = combo(input,7)
for i in final:
    if sum(i) == 100:
        #아래 대신 i.sort()해도 됨
        quick_sort(i)
        for j in i:
            print(j)
        break