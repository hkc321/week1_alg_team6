a, b = input().split(" ")

a_list = list(a)
b_list = list(b)

a_list.reverse()
b_list.reverse()

str_a = "".join(a_list)
str_b = "".join(b_list)

int_a = int(str_a)
int_b = int(str_b)

if(int_a > int_b) :
    print(int_a)
else :
    print(int_b)