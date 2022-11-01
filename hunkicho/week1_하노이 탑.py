# https://www.acmicpc.net/problem/1914

import sys
n = int(sys.stdin.readline())
def hanoi(n,x,y) -> None:
    #원반 n개를 x기둥에서 y기둥으로 옮긴다
    if n == 1:
        print(x,y)
        return

    hanoi(n-1,x,6-x-y) # 맨 아래 뺴고 중간에
    hanoi(1,x,y)  #맨 아래를 목표에
    hanoi(n-1,6-x-y,y) # 중간을 목표에

hanoi(n,1,3)
