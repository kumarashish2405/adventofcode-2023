import os

# part 1
def part1():

    numbers = {
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
    file_path = os.path.join(current_dir, 'inputnew1.txt')

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
      print(f" part 1 Result: {res}")



def part2():
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
        print(f" part 2 Result: {res}")


if __name__ == "__main__":
    part1()
    part2()
