def recover_calibration_values(calibration_document):
  calibration_values = []
  for line in calibration_document:
    line = line.strip()
    first_digit = int(line[0])
    last_digit = int(line[-1])
    calibration_value = int(str(first_digit) + str(last_digit))
    calibration_values.append(calibration_value)
  return calibration_values


def calculate_sum_of_calibration_values(calibration_document):
  calibration_values = recover_calibration_values(calibration_document)
  return sum(calibration_values)
