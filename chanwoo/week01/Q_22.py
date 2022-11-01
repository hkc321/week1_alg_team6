n = int(input())
sosu = []
a = [False, False] + [True] * (10000-1)
result = []
half = []

for i in range(2, 10000) :
    if a[i] :
        sosu.append(i)
        for j in range(i*2, 10000+1, i) :
            a[j] = False

for qw in range(n) :
    input_value=int(input())
    half.append(input_value // 2)

for k in range(n) :
    for j in range(half[k]) :
        x = half[k] + j
        y = half[k] - j

        if x in sosu and y in sosu :
            print(y, x)
            break