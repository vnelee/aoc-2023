import re

# input = 'example-input.txt'
input = 'input.txt'

with open(input) as file:
  filestr = file.read()

def possibleGame(line):
  line = line.replace(" ","")
  line = line.replace("Game", "")
  id = int(line.split(":")[0])

  """
  re.split result will result in
  [numCubes, color, numCubes, color, ... , None]
  pattern. Commas and semicolons are in the color
  string but won't matter
  """
  pulls = re.split(r"(\D+)", line.split(":")[1])

  i = 0
  numCubes = 0

  while i < len(pulls) - 1:
    if i%2 == 0:
      numCubes = int(pulls[i])
    else:
      match pulls[i][0]:
        case "r":
          if numCubes > 12:
            return 0
        case "g":
          if numCubes > 13:
            return 0
        case "b":
          if numCubes > 14:
            return 0
    i += 1

  return id

pt1 = 0

for line in filestr.strip().split('\n'):
  pt1 += possibleGame(line)

print("Part 1: " + str(pt1))

pt2 = 0

def fewestCubePower(line):
  line = line.replace(" ","")
  line = line.replace("Game", "")

  """
  re.split result will result in
  [numCubes, color, numCubes, color, ... , None]
  pattern. Commas and semicolons are in the color
  string but won't matter
  """
  pulls = re.split(r"(\D+)", line.split(":")[1])

  i = 0
  numCubes = 0
  rgb = [0,0,0]

  while i < len(pulls) - 1:
    if i%2 == 0:
      numCubes = int(pulls[i])
    else:
      match pulls[i][0]:
        case "r":
          rgb[0] = max(rgb[0], numCubes)
        case "g":
          rgb[1] = max(rgb[1], numCubes)
        case "b":
          rgb[2] = max(rgb[2], numCubes)
    i += 1

  return rgb[0] * rgb[1] * rgb[2]

for line in filestr.strip().split('\n'):
  pt2 += fewestCubePower(line)

print("Pt 2: " + str(pt2))