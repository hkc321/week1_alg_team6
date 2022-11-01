#https://www.acmicpc.net/problem/2588

def multi():
    a = int(input())
    b = int(input())

    strB1 = str(b)[0]
    strB2 = str(b)[1]
    strB3 = str(b)[2]

    print(a * int(strB3))
    print(a * int(strB2))
    print(a * int(strB1))
    print(a * b)

multi()

