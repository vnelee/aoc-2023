import re

# input = 'example-input.txt'
# input = 'example-input-pt2.txt'
input = 'input.txt'

with open(input) as file:
  filestr = file.read()

def cardPoints(line):
  line = re.sub(".*:", "", line)
  numList = re.sub(r"\s+", " ", line).split('|')
  winNums = set(numList[0].strip().split(" "))
  cardNums = numList[1].strip().split(" ")

  match = 0

  for num in cardNums:
    if num in winNums:
      match += 1

  if match > 0:
    return 2**(match - 1)
  else:
    return 0

pt1 = 0

for line in filestr.strip().split('\n'):
  pt1 += cardPoints(line)

print("Part 1: " + str(pt1))