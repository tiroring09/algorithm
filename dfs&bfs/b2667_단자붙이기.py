# https://www.acmicpc.net/problem/2667

import sys

sys.stdin = open('b2667.txt')

def dfs(x, y):
    # 현좌표할일
    visit[x][y] = True
    DG[-1] += 1

    # 다음탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if isIn(nx, ny) and matrix[nx][ny] == 1 and not visit[nx][ny]:
            dfs(nx, ny)

def isIn(x, y):
    return True if x in range(N) and y in range(N) else False

# 상하좌우
dx = [1,-1,0,0]
dy = [0,0,-1,1]

N = int(input())
matrix = [list(map(int, input())) for _ in range(N)]
visit = [[False for _ in range(N)] for _ in range(N)]
DG = []

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1 and not visit[i][j]:
            DG.append(0)
            dfs(i, j)

DG.sort()
print(len(DG))
for i in range(len(DG)):
    print(DG[i])