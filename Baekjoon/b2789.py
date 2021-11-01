from itertools import combinations

def solution():

  print('gwerw')
  
  n, m = map(int, input())

  l = list(map(int, input().split()))

  candidates = list(combinations(l, 3))

  print(candidates)

solution()