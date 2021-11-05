import sys

n, m = map(int, sys.stdin.readline().split())

nums = sorted(list(map(int, sys.stdin.readline().split())))
v = [False for _ in range(n)]

s = set()
l = []

def dfs(idx, depth):
  if len(l) == m:
    ret = l[:]

    s.add(tuple(ret))
    return
  
  for i in range(idx, n):
    if not v[i]:
      v[i] = True
      l.append(nums[i])
      dfs(i+1, depth+1)
      v[i] = False
      l.pop()

dfs(0, 0)

for i in sorted(list(s)):
  print(*i)