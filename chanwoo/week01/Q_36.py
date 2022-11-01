import sys
sys.setrecursionlimit(10000)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, h) :
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]

        if(0 <= nx < n) and (0 <= ny < n) :
            if list_map[nx][ny] > h and search_zone[nx][ny] == 0 :
                search_zone[nx][ny] = 1
                dfs(nx, ny, h)
            

n = int(sys.stdin.readline())
list_map = []
search_zone = []
ans = 0
m_h = 0

for i in range(n) :
    list_map.append(list(map(int, sys.stdin.readline().split())))

for i in list_map :
    temp = max(i)
    if m_h < temp :
        m_h = temp

for danger in range(m_h) : 
    cnt = 0
    search_zone = [[0] * n for a in range(n)]

    for i in range(n) :
        for j in range(n) :
            if list_map[i][j] > danger and search_zone[i][j] == 0:
                search_zone[i][j] = 1
                cnt += 1
                dfs(i, j, danger)

    if ans < cnt :
        ans = cnt

print(ans)