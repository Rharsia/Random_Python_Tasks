import re

file_path = '/Users/yichengzhang/Documents/GitHub/Random_Python_Tasks/advent_of_code/2023/day_1/input.txt'

with open(file_path, 'r') as file:
    calibration_values = [line.strip() for line in file.readlines()]


def extract_first_and_last_numbers(input_string):
    numbers = re.findall(r'\d', input_string)

    first_number = numbers[0]
    last_number = numbers[-1]

    value = int(first_number + last_number)
    return value

sum = 0
for line in calibration_values:
    sum += extract_first_and_last_numbers(line)

print(sum)