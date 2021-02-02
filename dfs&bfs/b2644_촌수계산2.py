# https://www.acmicpc.net/problem/2644
# dfs + relation 배열

import sys

sys.stdin = open('b2644.txt')

def dfs(v, cnt):
    visit[v] = True
    relation[v] = cnt

    for i in range(1, N+1):
        if matrix[v][i] == 1 and not visit[i]:
            dfs(i, cnt+1)

N = int(input())
FROM, TO = map(int, input().split())

matrix = [[0 for _ in range(N+1)] for _ in range(N+1)]
visit = [False for _ in range(N+1)]
relation = [-1 for _ in range(N+1)] # FROM 으로부터 각 정점에 이르는 거리, 기본값-1

M = int(input())
for _ in range(M):
    x, y = map(int, input().split())
    matrix[x][y] = matrix[y][x] = 1

dfs(FROM, 0)
print(relation[TO])