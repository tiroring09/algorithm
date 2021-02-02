import sys

sys.stdin = open('b5014.txt')

from collections import deque

# 전체층, 시작위치, 목적지, 위, 아래
F, S, G, U, D = map(int, input().split())
visit = [-1] * 1000001

def search(start):
  dq = deque([start])
  visit[start] = 0

  while dq:
    v = dq.popleft()

    if v == G:
      return visit[v]

    for nv in (v+U, v-D):
      if nv in range(1, F+1) and visit[nv] == -1:
        visit[nv] = visit[v] + 1
        dq.append(nv)

  return 'use the stairs'

print(search(S))