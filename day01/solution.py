# input = 'example-input.txt'
# input = 'example-input-pt2.txt'
input = 'input.txt'

with open(input) as file:
  filestr = file.read()

def getCalibrationValue(line):
  ret = ''
  for c in line:
    if c.isdigit():
      ret += c
      break
  for c in reversed(line):
    if c.isdigit():
      ret += c
      break
  return int(ret)

pt1 = 0

for line in filestr.strip().split('\n'):
  pt1 += getCalibrationValue(line)

print("Pt 1: " + str(pt1))

digits = {
  'one':'1',
  'two':'2',
  'three':'3',
  'four':'4',
  'five':'5',
  'six':'6',
  'seven':'7',
  'eight':'8',
  'nine':'9',
}

def getRealCalVal(line):
  ret = ''
  s = ''

  for c in line:
    digit = ''
    s += c

    if c.isdigit():
      digit = c
    else:
      for k in digits.keys():
        if s.endswith(k):
          digit = digits[k]

    if digit:
      if len(ret) == 2:
        ret = ret[:-1] + digit
      else:
        ret += digit

  if len(ret) == 1:
    ret += ret
  return int(ret)

pt2 = 0

for line in filestr.strip().split('\n'):
  pt2 += getRealCalVal(line)

print("Pt 2: " + str(pt2))