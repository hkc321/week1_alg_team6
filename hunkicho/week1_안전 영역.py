# https://www.acmicpc.net/problem/2468

import sys

c = int(sys.stdin.readline())
input = []
    
for i in range(c):
    input.append(list(map(int, sys.stdin.readline().split())))

for i in range(c):
    for j in range(c):
        if input[i][j] <= c:
            input[i][j] = "False"

for k in input:
    print(k)