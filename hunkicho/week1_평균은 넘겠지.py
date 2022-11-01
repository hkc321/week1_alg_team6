# https://www.acmicpc.net/problem/4344

# 실패 -> 라운드 함수 두번쨰 인자 바깥에 작성
# import sys

# count = int(sys.stdin.readline())

# for _ in range(count):
#     num = [int(x) for x in input().split()]
#     base = num[0]
#     del num[0]

#     print(str(round(base/sum(num)),3)+"%")

# 실패 -> 나누기 반대로 작성
# import sys

# count = int(sys.stdin.readline())

# for _ in range(count):
#     num = [int(x) for x in input().split()]
#     base = num[0]
#     del num[0]

#     print(sum(num)/base)

#     print(str(round(base/sum(num),3))+"%")


# 실패 -> 백분율 안함
# import sys

# count = int(sys.stdin.readline())

# for _ in range(count):
#     num = [int(x) for x in input().split()]
#     base = num[0]
#     del num[0]

#     print(sum(num)/base)

#     print(str(round(sum(num)/base,3))+"%")


# 실패-> 문제 잘못 이해해서 점수 평균 구했다
# import sys

# count = int(sys.stdin.readline())

# for _ in range(count):
#     num = [int(x) for x in input().split()]
#     base = num[0]
#     del num[0]

#     print(str(round(sum(num)/base,3)*100)+"%")

# 실패-> 반올림 먼저함
# import sys

# count = int(sys.stdin.readline())

# for _ in range(count):
#     num = [int(x) for x in input().split()]
#     base = num[0]
#     del num[0]
#     count_stu = 0

#     avg = sum(num)/base
#     for i in num:
#         if i > avg:
#             count_stu += 1
#     print(str(round(count_stu/base,3)*100)+"%")


# 실패 -> 맞아 떨어지는거 소수점 표시 안함
# import sys

# count = int(sys.stdin.readline())

# for _ in range(count):
#     num = [int(x) for x in input().split()]
#     base = num[0]
#     del num[0]
#     count_stu = 0

#     avg = sum(num)/base
#     for i in num:
#         if i > avg:
#             count_stu += 1
            
#     print(str(round((count_stu/base)*100,3))+"%")


# 맞춘거
# import sys

# count = int(sys.stdin.readline())

# for _ in range(count):
#     num = [int(x) for x in input().split()]
#     base = num[0]
#     del num[0]
#     count_stu = 0

#     avg = sum(num)/base
#     for i in num:
#         if i > avg:
#             count_stu += 1
            
#     print(format(round((count_stu/base)*100,3),".3f")+"%")


# 성능개선 (남이 한거)
# 점수 받을 때 map이랑 리스트로 받기, 리스트 슬라이싱, 소수점 표기법
import sys

C = int(sys.stdin.readline())

P = []

for i in range(C):
    P = []
    score = list(map(int,sys.stdin.readline().split()))
    tot = sum(score[1:])/score[0]
    for i in score[1:]:
        if i > tot:
            P.append(i)
        else:
            pass
    print(f'{len(P)/score[0] * 100:.3f}%')  
