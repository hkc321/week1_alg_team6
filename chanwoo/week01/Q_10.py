n, x = map(int, input().split())

input_list = list(map(int, input().split()))
num_list = []

for i in range(n) :
    if (input_list[i] < x) :
        num_list.append(input_list[i])
for j in num_list :
    print(j, end=" ")