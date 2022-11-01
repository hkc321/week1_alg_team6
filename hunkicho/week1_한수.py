# https://www.acmicpc.net/problem/1065

# 1자리랑 2자리인거 포함 안함
# # import sys
# input_number = int(sys.stdin.readline())

# if input_number <= 9:
#     print("len",len(input_number))
#     print(9)
# elif input_number <= 99:
#     print(len(input_number))
#     print(99)
# else:
#     if int(str(input_number)[0:1])  % 2 == 0:
#         print("first1,",str(input_number)[0:1] )
#         print((int(str(input_number)[0:1]) // 2) * 2)
#     else:
#         print("first2,",str(input_number)[0:1] )
#         print(( ( int(str(input_number[0:1])) // 2) * 2) + 1)


import sys
input_number = int(sys.stdin.readline())

if input_number <= 98:
    print(input_number)
elif input_number <= 110:
    print(99)
else:
    sum = 0
    
    for k in range(111,input_number + 1):
        test = []
        for i in range(len(str(k))):
            globals()['a{}'.format(i)] = int(str(k)[i])

        for j in range(len(str(k))-1):
            test.append( globals()['a{}'.format(j)] - globals()['a{}'.format(j+1)])
        
        test = list(set(test))
        
        if len(test) == 1:
            sum += 1
    print(99 + sum)








# 9 5 4 
# 8 4 0
# 7 4 1
# 6 3 0
# 5 3 1
# 4 2 0
# 3 2 1
# 2 1 0
# 1 1 1