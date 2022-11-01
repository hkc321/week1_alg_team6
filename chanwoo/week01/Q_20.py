import sys
a, b, v = map(int, sys.stdin.readline().split(" "))

day = 0

b_dis = v - a

if b_dis % (a-b) != 0 :
    day = ((b_dis) // (a-b)) + 1
else :
    day = ((b_dis) // (a-b))

day += 1
print(day)