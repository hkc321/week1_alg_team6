n = int(input())
n_1 = 0
n_2 = 0
n_3 = 0
hansu = 0

for i in range(1, n+1) :
    if i < 10 :
        hansu += 1
    elif i < 100 :
        hansu += 1
    else :
        n_3 = i // 100
        n_2 = (i%100) // 10
        n_1 = i % 10
        if (n_3 - n_2 == n_2 - n_1) :
            hansu += 1

print(hansu)