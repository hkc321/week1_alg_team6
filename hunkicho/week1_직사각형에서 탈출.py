#https://www.acmicpc.net/problem/1085


#2번 째 성공
#이유: 정방향 거리만 생각, 역방향 생각 안함
def get_fast_route():
    x,y,w,h = map(int, input().split())

    w_posi = abs(w - x)
    h_posi = abs(h - y)

    width = w_posi if w_posi < x else x
    height = h_posi if h_posi < y else y

    print(width if width < height else height)

get_fast_route()