import sys
sys.stdin = open('b9205.txt')

def search(cv):
    global REACHED

    if cv == V[-1]:
        REACHED = True
        return

    for i in range(N+2):
        nv = V[i]
        if isReachable(cv, nv) and not visit[i] and not REACHED:
            visit[i] = True
            search(nv)

def isReachable(v1, v2):
    return abs(v1[0]-v2[0]) + abs(v1[1]-v2[1]) <= 1000

T = int(input())    #테케수
for tc in range(T):
    N = int(input())    #편의점수
    V = [tuple(map(int, input().split())) for _ in range(N+2)]  # 집, 편의점들, 목적지 좌표의 리스트
    visit = [False for _ in range(N+2)]

    REACHED = False
    visit[0] = True
    search(V[0])
    print('happy' if REACHED else 'sad')