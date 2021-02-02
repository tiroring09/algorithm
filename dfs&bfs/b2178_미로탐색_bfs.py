# https://www.acmicpc.net/problem/2178

import sys

sys.stdin = open('b2178.txt')

# 상하좌우
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = list()
    q.append((x, y))
    visited[x][y] = True
    result[x][y] = 1

    while q:
        cx, cy = q.pop(0)
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if nx >= 0 and nx < N and ny >= 0 and ny < M and not visited[nx][ny] and matrix[nx][ny] == 1:
                result[nx][ny] = result[cx][cy] + 1
                q.append((nx, ny))
                visited[nx][ny] = True


N, M = map(int, input().split())
matrix = [list(map(int, input())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
result = [[0 for _ in range(M)] for _ in range(N)]

bfs(0, 0)
print(result[N-1][M-1])