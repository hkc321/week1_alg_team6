# https://www.acmicpc.net/problem/2750

# 퀵정렬
import sys

def qsort(num,left,right) -> None:
    print("num=",num)
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

count = int(sys.stdin.readline())
num = [0] * count

for i in range(count):
    num[i] = int(sys.stdin.readline())

quick_sort(num)

for i in num:
    print(i)