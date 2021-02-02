# https://www.acmicpc.net/problem/1260

import sys

sys.stdin = open('b1260.txt')

def dfs(x):
    result.append(x)
    visited[x] = True

    for i in range(N+1):
        if not visited[i] and matrix[x][i] == 1:
            dfs(i)

def bfs(x):
    q = list()

    q.append(x)
    visited[x] = True

    while q:
        nx = q.pop(0)

        result.append(nx)

        for i in range(N+1):
            if not visited[i] and matrix[nx][i] == 1:
                q.append(i)
                visited[i] = True


N, M, V = map(int, input().split()) # 정점 수, 간선 수, 시작위치
matrix = [[0 for _ in range(N+1)] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
result = []

for i in range(M):
    x, y = map(int, input().split())
    matrix[x][y] = matrix[y][x] = 1
# input loaded

dfs(V)
print(' '.join(map(str, result)))

visited = [False for _ in range(N+1)]
result = []

bfs(V)
print(' '.join(map(str, result)))