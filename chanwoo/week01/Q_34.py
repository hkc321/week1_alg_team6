from itertools import permutations


n = int(input())
num_list = list(map(int, input().split()))

com = permutations(num_list, n)
sum_max = 0

for i in com :
    s = 0
    for j in range(len(i)-1) :
        s += abs(i[j]-i[j+1])
    if s > sum_max :
        sum_max = s

print(sum_max)