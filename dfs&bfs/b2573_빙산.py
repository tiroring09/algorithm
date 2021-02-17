import sys
sys.stdin = open('b2573.txt')

from collections import deque
# import sys
# sys.setrecursionlimit(100000)

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
    # 현시점 빙산이 한 덩어리인지 여부 출력. 이 때 빙산이 몇 덩어리인지 완전탐색한 후, 결과를 출력하는 방식을 택하면 python3에서 시간초과 및 recursion오류. pypy3에서는 통과.
    # 두번째 빙산덩어리를 발견하는 순간 탈출하는 방식을 택해도 python3에서 시간초과 확인. 아예 다른방식으로 접근해야 할 듯.
    visit = [ [False] * M for _ in range(N) ]
    foundOne = False
    for i in range(N):
        for j in range(M):
            if matrix[i][j] != 0 and not visit[i][j]:
                if foundOne:
                    return False
                else:
                    foundOne = True
                    visit[i][j] = True
                    # dfs(i, j, visit)
                    bfs(i, j, visit)
    return True

# def isOne():
#     visit = [ [False] * M for _ in range(N) ]
#     cnt = 0
#     for i in range(N):
#         for j in range(M):
#             if matrix[i][j] != 0 and not visit[i][j]:
#                 cnt += 1
#                 visit[i][j] = True
#                 # dfs(i, j, visit)
#                 bfs(i, j, visit)
#     return True if cnt == 1 else False

def dfs(x, y, visit):
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
        if isMeltAll():
            return 0
        if not isOne():
            return year

print(main())