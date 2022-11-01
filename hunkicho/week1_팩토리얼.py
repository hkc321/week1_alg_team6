# https://www.acmicpc.net/problem/10872

import sys

def fac(n):
    if n > 0:
        return n * fac(n-1)
    else:
        return 1

m = int(sys.stdin.readline())
print(fac(m))