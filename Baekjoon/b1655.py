import heapq
import sys

n = int(sys.stdin.readline())

left, right = [], []

for _ in range(n):
  num = int(sys.stdin.readline())

  if len(left) == len(right):
    heapq.heappush(left, (-num, num))
  else:
    heapq.heappush(right, (num, num))

  if right and left[0][1] > right[0][1]:
    lv = heapq.heappop(left)[1]
    rv = heapq.heappop(right)[1]

    heapq.heappush(left, (-rv, rv))
    heapq.heappush(right, (lv, lv))
  
  print(left[0][1])
