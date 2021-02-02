# https://www.acmicpc.net/problem/2644
# bfs

import sys

sys.stdin = open('b2644.txt')

from collections import deque

def bfs():
    dq = deque()
    dq.append(FROM)
    visit[FROM] = True

    while dq:
        v = dq.popleft()
        # if v == TO:
        #     break

        for i in range(1, N+1):
            if matrix[v][i] == 1 and not visit[i]:
                visit[i] = True
                relation[i] = relation[v] + 1
                dq.append(i)

N = int(input())
FROM, TO = map(int, input().split())

matrix = [[0 for _ in range(N+1)] for _ in range(N+1)]
visit = [False for _ in range(N+1)]
relation = [-1 for _ in range(N+1)]  # FROM 으로부터 각 정점까지 이르는 거리
relation[FROM] = 0

M = int(input())
for _ in range(M):
    x, y = map(int, input().split())
    matrix[x][y] = matrix[y][x] = 1

bfs()
print(relation[TO])