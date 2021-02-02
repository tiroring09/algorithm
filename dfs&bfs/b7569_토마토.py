# https://www.acmicpc.net/problem/7569

import sys

sys.stdin = open('b7569.txt')

from collections import deque

M, N, H = map(int, input().split())
matrix = [ [ list(map(int, input().split())) for _ in range(N) ] for _ in range(H) ]

# for i in range(H):
#     for j in range(N):
#         print(matrix[i][j])
#     print()

# 위아래 상하 좌우
dx = [1, -1, 0, 0, 0, 0 ]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def isIn(x, y, z):
    return x in range(H) and y in range(N) and z in range(M)
    # return 0<=x and x<H and 0<=y and y<N and 0<=z and z<M

def check():
    _max = 0
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if matrix[i][j][k] > _max:
                    _max = matrix[i][j][k]
                if matrix[i][j][k] == 0:
                    return -1
    return _max - 1

# bfs
dq = deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if matrix[i][j][k] == 1:
                dq.append((i, j, k))

while dq:
    cx, cy, cz = dq.popleft()

    for i in range(6):
        nx = cx + dx[i]
        ny = cy + dy[i]
        nz = cz + dz[i]
        if isIn(nx, ny, nz) and matrix[nx][ny][nz] == 0:
            matrix[nx][ny][nz] = matrix[cx][cy][cz] + 1
            dq.append((nx, ny, nz))


# for i in range(H):
#     for j in range(N):
#         print(matrix[i][j])
#     print()

print(check())