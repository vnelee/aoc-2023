import re

# input = 'example-input.txt'
input = 'input.txt'

with open(input) as file:
  filestr = file.read()

matrix = filestr.strip().split('\n')
row = len(matrix)
col = len(matrix[0])

def partNumber(i,j1,j2,num):
  for (x,y) in ([(r,j1-1) for r in range(i-1,i+2)] + [(r,j2+1) for r in range(i-1,i+2)]
                + [(i-1,j) for j in range(j1,j2+1)] + [(i+1,j) for j in range(j1,j2+1)]):
    if 0<=x<row and 0<=y<col and matrix[x][y] != "." and not matrix[x][y].isdigit():
      return num
  return 0

stars = {}

def gearRatio(i,j1,j2,num):
  for (x,y) in ([(r,j1-1) for r in range(i-1,i+2)] + [(r,j2+1) for r in range(i-1,i+2)]
                + [(i-1,j) for j in range(j1,j2+1)] + [(i+1,j) for j in range(j1,j2+1)]):
    if 0<=x<row and 0<=y<col and matrix[x][y] == "*":
      if (x,y) in stars:
        return stars[(x,y)] * num
      else:
        stars[(x,y)] = num
        return 0
  return 0

pt1 = 0
pt2 = 0

for i,line in enumerate(filestr.strip().split('\n')):
  # nums is list of (start idx of number, end idx of number, number) tuples
  nums = [(m.start(0), m.end(0)-1, int(m.group(0))) for m in re.finditer("\d+", line)]
  for (j1,j2,num) in nums:
    pt1 += partNumber(i,j1,j2,num)
    pt2 += gearRatio(i,j1,j2,num)
  i+=1

print("Pt 1: " + str(pt1))
print("Pt 2: " + str(pt2))