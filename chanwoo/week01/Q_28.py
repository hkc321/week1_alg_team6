#1사분면 row < (array_size / 4) col < (array_size / 4) 1 : 0 4*0
#2사분면 row > (array_size / 4) col < (array_size / 4) 1 : 16 4*4 
#3사분면 row < (array_size / 4) col > (array_size / 4) 1 : 32 4*8
#4사분면 row > (array_size / 4) col > (array_size / 4) 1 : 48 4*12

# n = 2 일때 
#            1 : 0 4*0 
#            2 : 4 4*1 
#            3 : 8 4*2
#            4 : 12 4*3

import sys
sys.setrecursionlimit(10**8)

def fuction_z(value_max, value_min, row, col, n) :
    result = 0
    half = 2 ** (n-1)
    if (n == 1) :
        if row < (half) and col < (half) :
            result = value_min
        elif row == (half) and col < (half) :
            result = value_min + 1
        elif row < (half) and col == (half) :
            result = value_min + 2
        elif row == (half) and col == (half) :
            result = value_min + 3
        print(result)
        return 0

    quarter = 2 ** ((2 * n) - 2)

    if row < (half) and col < (half) :
        value_max = value_min + quarter
        value_min = value_max - quarter
    elif row >= (half) and col < (half) :
        value_max = value_min + (quarter * 2)
        value_min = value_max - quarter
        row -= half
    elif row < (half) and col >= (half) :
        value_max = value_min + (quarter * 3)
        value_min = value_max - quarter
        col -= half
    elif row >= (half) and col >= (half) :
        value_max = value_min + (quarter * 4)
        value_min = value_max - quarter
        row -= half
        col -= half

    fuction_z(value_max, value_min, row, col, n-1)

n, row, col = map(int, input().split())

list_max = (2 ** (n*2))

fuction_z(list_max, 0, col, row, n)