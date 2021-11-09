pan = []

nums = [i for i in range(1, 10)]
zero_pos = {}

for _ in range(9):
  pan.append(list(map(int, input().split())))

def row_check(l, r):
  for i in range(9):
    if pan[r][i] in l:
      l.remove(pan[r][i])
  
  return l

def col_check(l, c):
  for i in range(9):
    if pan[i][c] in l:
      l.remove(pan[i][c])
  return l

def squre_check(i, j, l):
  r = (i // 3)*3
  c = (j // 3)*3

  for i in range(r, r+3):
    for j in range(c, c+3):
      if pan[r][c] in l:
        l.remove(pan[r][c])
  
  return l

for i in range(9):
  for j in range(9):
    if pan[i][j] == 0:
      zero_pos[(i,j)] = [k for k in range(1, 10)]

for pos in zero_pos.items():
  i, j = pos[0]
  l = pos[1]

  l = row_check(l, i)
  l = col_check(l, j)
  l = squre_check(i, j, l)

  zero_pos[(i,j)] = l

  #pan[i][j] = l[0]

print(zero_pos)

print()

for i in pan:
  for j in i:
    print(j, end= ' ')
  print()