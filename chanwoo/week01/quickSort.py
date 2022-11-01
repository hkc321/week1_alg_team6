#a -> 정렬할 배열, p -> 첫번째 원소 위치, q -> 마지막 원소 위치

def quickSort(a, p, r) :
    if (p < r) :
        q = partition(a, p, r)
        quickSort(a, p, q-1)
        quickSort(a, q+1, r)

def partition(a, p, r) : #a[r] 기준으로 재배치, a[r] 이 위치한 위치 리턴
    point = a[r]
    i = p-1 #1구역 위치
    for j in range(p, r, 1) : #3구역 위치
        if (a[j] <= point) : #1구역으로 보내기
            i += 1
            a[i], a[j] = a[j], a[i]            

    a[i+1], a[r] = a[r], a[i+1] # 기준원소를 1구역 뒤(2구역 앞)으로 보내기
    return i+1 #기준원소 (4구역) 위치

n = int(input())
a = []

for i in range(n) :
    a.append(int(input()))

quickSort(a, 0, n-1)

for i in a :
    print(i)