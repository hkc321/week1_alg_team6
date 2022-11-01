a = []

for i in range(9) :
    a.append(int(input()))

max = 0
index = 0

for j in range(9) :
    if (a[j] > max) :
        max = a[j]
        index = j+1

print(max)
print(index)