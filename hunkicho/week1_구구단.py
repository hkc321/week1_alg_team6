#https://www.acmicpc.net/problem/2739

#처음 실패
# def multiplication_table():
#     n = int(input())

#     for i in range(1,10):
#         print(n, " * ", i, " = ", n * i )

#multiplication_table()
#이유: 출력시 띄어쓰기 잘못-> ,사용시 자동으로 한칸 공백

def multiplication_table():
    n = int(input())

    for i in range(1,10,1):
        print(n, "*", i, "=", n * i )

multiplication_table()