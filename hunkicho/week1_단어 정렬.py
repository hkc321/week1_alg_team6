# https://www.acmicpc.net/problem/1181
# https://blockdmask.tistory.com/543
# set을 이용하면 중복이 제거됨
# https://always-challenger-lab.tistory.com/22
# 람다 이용해서 다중조건 정렬
import sys

n = int(sys.stdin.readline())
s = []
m = []
for i in range(n):
    s.append(str(sys.stdin.readline().strip()))


set_s = list(set(s))
for j in set_s:
    m.append([j,len(j)])

print(m)
m.sort(key=lambda x:(x[1],x[0]))

for i in m:
    print(i[0])