n = int(input())
list_input_text = []
repeat = []

for i in range(n) : 
    input_num, input_text = input().split(" ")
    repeat.append(input_num)
    list_input_text.append(list(input_text))

for j in range(n) :
    for k in range(len(list_input_text[j])) :
        for l in range(int(repeat[j])) :
            print(list_input_text[j][k], end="")
    print()