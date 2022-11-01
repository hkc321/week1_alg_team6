import copy
input_row, input_col = map(int, input().split())
row = []
col = []
position = 0

for i in range(input_row) :
    row.append(i)

for i in range(input_col) :
    col.append(i)

n = int(input())
for i in range(n) :
    split_index, split_value = map(int, input().split())
    if split_index == 0 :
        position = col.index(split_value)
        col.insert(position, -1)
    else :
        position = row.index(split_value)
        row.insert(position, -1)

row.append(-1)
col.append(-1)

row_max = 0
col_max = 0
temp = 0
temp2 = 0

for i in row :
    if (i == -1) :
        if row_max < temp :
            row_max = temp
            temp = 0
        else :
            temp = 0
    else :
        temp += 1

for i in col :
    if (i == -1) :
        if col_max < temp2 :
            col_max = temp2
            temp2 = 0
        else :
            temp2 = 0
    else :
        temp2 += 1

print(row_max * col_max)