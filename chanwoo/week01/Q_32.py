n = int(input())
input_list = []
array = [[] for i in range(50)]
no_overlap_array = [[] for i in range(50)]


for i in range(n) :
    input_value = input()
    array[len(input_value)-1].append(input_value)

for i in range(50) :
    array[i].sort()
    no_overlap_array[i] = list(dict.fromkeys(array[i]))

for i in range(50) :
    for j in no_overlap_array[i] :
        print(j)
