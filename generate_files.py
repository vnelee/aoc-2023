# Generate directory for a new day with empty example-input.txt and solution.py files

import sys
import os

if len(sys.argv) < 2:
  raise ValueError("Please provide day for which to make directory.")

day = int(sys.argv[1])

if day < 1 or day > 25:
  raise ValueError(f"Invalid day. Should be between 1 and 25 (Value provided: {day})")

if day < 10:
  dirname = "day0" + str(day)
else:
  dirname = "day" + sys.argv[1]

curr_dir = os.getcwd()
new_dir = os.path.join(curr_dir, dirname)

print("Making new directory: ./" + dirname)
os.mkdir(new_dir)

os.chdir(new_dir)
open("example-input.txt","w").close()
open("solution.py","w").close()