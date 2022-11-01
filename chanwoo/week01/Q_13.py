n = int(input())
b = []
a_age = []
s_sum = []
p_pass = []

for i in range(n) :
    a = list(map(int, input().split()))
    b.append(a)

for j in range(n) :
    s_sum.append(sum(b[j]) - b[j][0])

for k in range(n) :
    a_age.append(s_sum[k] / b[k][0] )

for x in range(n) :
    