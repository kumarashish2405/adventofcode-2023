import os
import re

YEAR = 2023
DAY = 1

numbers = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'inputnew2.txt')

with (open(file_path, "r")) as f:
  input = (f.read().splitlines())
  res = 0
  left = ""
  right = ""
  for line in input:
    calibration = 0
    for i in range(0, len(line)):
      for j in range(i, len(line)):
        if line[i:j + 1] in numbers:
          if not left:
            left = line[i:j + 1]
          right = line[i:j + 1]
    calibration = numbers[left] * 10 + numbers[right]
    left = ""
    res += calibration
  print(f"{YEAR} {DAY} part 2 Result: {res}")
