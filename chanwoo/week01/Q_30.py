import sys
n = int(sys.stdin.readline())
number_list = [[0] for i in range(2000001)]

for i in range(n) :
    input_number = int(sys.stdin.readline())
    number_list[input_number + 1000000][0] = 1

for i in range(2000001) :
    if (number_list[i][0] == 1) :
        print(i-1000000)