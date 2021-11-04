from itertools import permutations

n, m = map(int, input().split())

l = []

def dfs():
  if len(l) == m:
    print(' '.join(map(str, l)))
  
  for i in range(1, n+1):
    if i not in l:
      l.append(i)
      dfs()
      l.pop()

dfs()
