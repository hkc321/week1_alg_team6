T = int(input())
a = []
b = []
c = []

for i in range(T) :
    A, B = map(int, input().split())
    a.append(A)
    b.append(B)
    c.append(a[i] + b[i])

for j in range(T) :
    print(c[j])