#36 가지 경우의 수 존재
# 1, (2~9) 8 1,2 1,3 1, 4
# 2, (3~9) 7
# 3, (4~9) 6
# 4, (5~9) 5
# 5, (6~9) 4
# 6, (7~9) 3
# 7, (8~9) 2
# 8, (9) 1
# 9, 0
input_list = []
for_break = False

for i in range(9) :
    input_list.append(int(input()))

for i in range(9) :
    for j in range(i+1, 9, 1) :
        if (sum(input_list) - (input_list[i] + input_list[j])) == 100 :
            input_list[i] = 0
            input_list[j] = 0
            for_break = True
            break
    if for_break == True:
        break


input_list.sort()

for i in input_list :
    if i != 0 :
        print(i)
