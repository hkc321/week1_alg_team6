# https://www.acmicpc.net/problem/2628

import sys

length = list(map(int, sys.stdin.readline().split()))
cut_count = int(sys.stdin.readline())
w = []
h = []
hap = []


for i in range(cut_count):
    cut = list(map(int, sys.stdin.readline().split()))
    if cut[0] == 0:
        w.append(cut[1])
    else:
        h.append(cut[1])

w.append(length[1])
w.append(0)
h.append(length[0])
h.append(0)
            
w.sort()
h.sort()

for i in range(len(w)-1):
    for j in range(len(h)-1):
        hap.append(abs(w[i] - w[i+1]) * abs(h[j] - h[j+1]))

print(max(hap))
