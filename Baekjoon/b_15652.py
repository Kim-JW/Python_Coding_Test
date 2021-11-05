import sys

n, m = map(int, sys.stdin.readline().split())
l = []

def dfs(idx):
  if len(l) == m:
    print(' '.join(map(str, l)))
    return
  
  for i in range(idx, n+1):
    l.append(i)
    dfs(i)
    l.pop()

dfs(1)