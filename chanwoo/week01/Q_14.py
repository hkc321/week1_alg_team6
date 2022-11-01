a = int(input())
b = int(input())
c = int(input())

count = []
c_count = 0

result = str(a * b * c)
list_result = list(result)

for i in range(0, 10) :
    c_count = 0
    for j in list_result:
        if str(i) == j :
            c_count += 1
    count.append(c_count)

for k in count :
    print(k)