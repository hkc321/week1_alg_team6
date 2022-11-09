import sys

prime_list = [False, False] + [True]*10002
#입력값은 10000까지 주어지며 0, 1번 인덱스는 False인 소수리스트를 만든다. 

for i in range(2, 10002):
    if prime_list[i]:
        for j in range(2*i, 10002, i):
        #소수를 구하기 위해 반복문을 돌린다. 10002보다 작지만 2의 배수들은 소수가 아니니 False값을 담는다. 
            prime_list[j] = False

T = int(sys.stdin.readline()) #입력받는 테스트 케이스의 개수 T

for i in range(T):
    n = int(sys.stdin.readline()) #입력받는 짝수 n
    a = n // 2 #입력받은 짝수의 중간값을 만들어 탐색한다.
    b = a
    while a > 0:
        if prime_list[a] and prime_list[b]:
        #a와 b가 소수일 때 True를 반환하므로 a, b를 출력한다.
            print(a, b)
            break
        else:
            a -= 1
            b += 1