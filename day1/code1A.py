import os
import re


def get_score(input):
  score = 0
  entry = re.findall(r'\d{1}', input)
  score = int(entry[0]) * 10 + int(entry[-1])
  return score


def code1A():
  print("START - code1A")

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
  print("END - code1A")
