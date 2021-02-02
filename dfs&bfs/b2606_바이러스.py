# https://www.acmicpc.net/problem/2606
import sys

sys.stdin = open('b2606.txt')

def bfs(start):
    cnt = 0

    q = list()
    q.append(start)
    visited[start] = True

    while q:
        now = q.pop(0)

        for i in range(1, N+1):
            if matrix[now][i] == 1 and not visited[i]:
                cnt += 1
                q.append(i)
                visited[i] = True

    return cnt

N = int(input())
K = int(input())

matrix = [[0 for _ in range(N+1)] for _ in range(N+1)]
visited = [False for _ in range(N+1)]

for _ in range(K):
    x, y = map(int, input().split())
    matrix[x][y] = 1
    matrix[y][x] = 1

print(bfs(1))