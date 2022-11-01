#countinSort
import sys
input = sys.stdin.readline

n = int(input())

count = [0] * 10000

for i in range(n) :
    input_value = int(input())
    count[input_value-1] += 1

for i in range(10000) :
    if count[i] != 0 :
        for j in range(count[i]) :
            print(i+1)