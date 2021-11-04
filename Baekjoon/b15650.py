from itertools import permutations

n, m = map(int, input().split())

l = []

def dfs():
  if len(l) == m:
    tmp = 0

    for i in range(len(l)):
      if tmp > l[i]:
        break
      else:
        tmp = l[i]
    else:
      print(' '.join(map(str, l)))
  
  for i in range(1, n+1):
    if i not in l:
      l.append(i)
      dfs()
      l.pop()

dfs()

