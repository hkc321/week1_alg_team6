def bubbleSort(a, n) :
    for last in range(n, 1, -1) :
        for j in range(0, last-1, 1) :
            if(a[j] > a[j+1]) : a[j], a[j+1] = a[j+1], a[j]

n = int(input())
a = []

for i in range(n) :
    a.append(int(input()))

bubbleSort(a, n-1)

for i in a :
    print(i)