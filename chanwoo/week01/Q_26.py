def hanoi(n, start, temp, end) :
    if(n==1) :
        print(start, end)
        return 1
    hanoi(n-1, start, end, temp)
    print(start, end)
    hanoi(n-1, temp, start, end)

n = int(input())

print((2 ** n)-1)
if n <= 20 :
    hanoi(n, '1', '2', '3')