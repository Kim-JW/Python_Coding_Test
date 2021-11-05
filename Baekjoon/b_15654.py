import sys

n, m = map(int, sys.stdin.readline().split())

nums = sorted(list(map(int, sys.stdin.readline().split())))

l = []

def dfs():
  if len(l) == m:
    print(' '.join(map(str, l)))
    return
  
  for i in range(n):
    if nums[i] not in l:
      l.append(nums[i])
      dfs()
      l.pop()

dfs()