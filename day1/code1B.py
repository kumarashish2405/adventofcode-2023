import os
import re

valid_spells = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}


# Single Input Line
def get_digits(line):
  digits = []
  for index, char in enumerate(line):
    if char.isdigit():
      digits.append(int(char))
    else:
      value = -1
      tmp = line[index:min(index + 5, len(line))]
      for x in valid_spells.keys():
        if tmp.find(x) == 0:
          value = valid_spells[x]
          break
      if value > -1:
        digits.append(value)

  return digits


def get_score(input):
  score = 0
  entry = get_digits(input)
  score = int(entry[0]) * 10 + int(entry[-1])
  return score


def code1B():
  print("START - code1B")

  # Data - Input
  current_dir = os.path.dirname(os.path.abspath(__file__))
  file_path = os.path.join(current_dir, 'sampleInput.txt')
  input = []
  with (open(file_path, "r")) as f:
    # Read the file line by line
    input = [line.strip() for line in f.readlines()]

  final_score = 0
  for line in input:
    final_score += get_score(line)

  print(final_score)
  print("END - code1B")
