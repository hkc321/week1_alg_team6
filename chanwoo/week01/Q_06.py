x, y, w, h = map(int, input().split())

up = h - y
down = y
right = w - x
left = x

distance = [up, down, right, left]
print(min(distance))