from itertools import permutations
import sys

n = int(sys.stdin.readline())
w = []
city = []

for i in range(n) :
    w.append(list(map(int, sys.stdin.readline().split())))
    city.append(i)

a = permutations(city, n)

m_min = 4000001

for i in a :
    temp = 0
    for j in range(n) :
        if j == (n-1) :
            distance = w[i[j]][i[0]]
        else :
            distance = w[i[j]][i[j+1]]
        if distance == 0 :
            temp = -1
            break
        else :
            temp += distance

    if temp != -1 and m_min > temp :
        m_min = temp

print(m_min)