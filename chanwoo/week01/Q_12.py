import sys
sys.setrecursionlimit(10**8)

n = int(input())
input_list = []
s_input_list = []
count = 0
temp = []
temp2 = []
temp3 = 0
score = []

def sum(n) :
    if n == 1 :
        return 1
    return n + sum(n-1)

for q in range(n) :
    s_input_list = list(input())
    input_list.append(s_input_list)

for q in range(n) :
    for i in range(len(input_list[q])) :
        if (input_list[q][i] == 'O') :
            count += 1
        elif (input_list[q][i] == 'X' and count != 0):
            temp2.append(count)
            count = 0
        else :
            count = 0

    temp2.append(count)
    temp.append(temp2)

# for j in range(n) :
#     pls = 0
#     temp3 = 0
#     for k in range(len(temp[j])) :
#         temp3 = temp[j][k]
#         pls += sum(temp3)

#     score.append(pls)

# for l in score :
#     print(l)