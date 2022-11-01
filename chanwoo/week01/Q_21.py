from cmath import sqrt
import math

def decide(b) :
    i = 2
    a=int(b)
    if a == 2 or a == 3:
        return True
    elif a == 1 :
        return False
    while i * i <= a :
        if a % i == 0 :
            return False
        i+=1
    return True

n = int(input())
a = input().split(" ")
count = 0

for i in range(n) :
    if decide(a[i]) == True :
        count += 1

print(count)