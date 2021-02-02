import sys
sys.stdin = open('b2573.txt')

from collections import deque

N, M = map(int, input().split())
matrix = [ list(map(int, input().split())) for _ in range(N) ]

# 상하좌우
dx = [1,-1,0,0]
dy = [0,0,-1,1]

def melt():
    cache = [[0] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if matrix[i][j] != 0:
                cache[i][j] = countWater(i, j)
    
    for i in range(N):
        for j in range(M):
            matrix[i][j] = max(matrix[i][j] - cache[i][j], 0)

def countWater(x, y):
    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if matrix[nx][ny] == 0:
            cnt += 1
    return cnt

def isOne():
    visit = [ [False] * M for _ in range(N) ]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if matrix[i][j] != 0 and not visit[i][j]:
                cnt += 1
                visit[i][j] = True
                # dfs(i, j, visit)
                bfs(i, j, visit)
    return True if cnt == 1 else False

def dfs(x, y, visit):
    # visit[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if matrix[nx][ny] != 0 and not visit[nx][ny]:
            visit[nx][ny] = True
            dfs(nx, ny, visit)

def bfs(x, y, visit):
    dq = deque([(x, y)])

    while dq:
        cx, cy = dq.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if matrix[nx][ny] != 0 and not visit[nx][ny]:
                visit[nx][ny] = True
                dq.append((nx, ny))


def isMeltAll():
    for i in range(N):
        for j in range(M):
            if matrix[i][j] != 0:
                return False
    return True

def main():
    year = 0
    while True:
        year += 1
        melt()
        if not isOne():
            return year
        if isMeltAll():
            return 0

print(main())