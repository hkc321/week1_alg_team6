a = int(input())
b = int(input())

b_x = b // 100
b_y = (b-(100*b_x)) // 10
b_z = b % 10
b_digit = [b_x, b_y, b_z]

result = []

for i in b_digit :
    temp = a * i
    result.append(temp)

result.reverse()

for j in result :
    print(j)

print(a*b)