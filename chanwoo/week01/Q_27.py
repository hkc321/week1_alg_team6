global cnt
cnt = 0

def n_queen (col, i) :
    n = len(col) - 1
    if (judge(col, i)) :
        if(i==n) :
            print(col[1: n+1])
        else :
            for j in range(1, n+1) :
                col[i+1] = j
                n_queen(col, i+1, cnt)

    print(cnt)

def judge(col, i) :
    k = 1
    flag = True
    while (k < i and flag) :
        if (col[i] == col[k] or abs(col[i] - col[k]) == (i - k)) :
            flag = False
        k += 1
    return flag

n = 8
a = [0] * (n+1)
n_queen(a, 0, 0)