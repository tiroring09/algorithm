import sys

sys.stdin = open('b5014.txt')

from collections import deque

# 전체층, 시작위치, 목적지, 위, 아래
F, S, G, U, D = map(int, input().split())
visit = [False] * 1000001

def search(start):
  dq = deque([(start, 0)])
  visit[start] = True

  while dq:
    v, cnt = dq.popleft()

    if v == G:
      return cnt

    for nv in (v+U, v-D):
      if nv in range(1, F+1) and not visit[nv]:
        visit[nv] = True
        dq.append((nv, cnt+1))

  return 'use the stairs'

print(search(S))