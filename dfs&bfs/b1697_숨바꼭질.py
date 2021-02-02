import sys

sys.stdin = open('b1697.txt')

from collections import deque

def bfs(start):
  dq = deque([(start, 0)])
  visit[start] = True

  while dq:
    x, cnt = dq.popleft()

    if x == k:
      return cnt

    for new in (x-1, x+1, 2*x):
      if new in range(0, 100001) and not visit[new]:
        visit[new] = True
        dq.append((new, cnt+1))

n, k = map(int, input().split())
visit = [False] * 100001

print(bfs(n))