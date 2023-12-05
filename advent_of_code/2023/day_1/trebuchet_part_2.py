import re

file_path = '/Users/yichengzhang/Documents/GitHub/Random_Python_Tasks/advent_of_code/2023/day_1/input.txt'

with open(file_path, 'r') as file:
    calibration_values = [line.strip() for line in file.readlines()]

number_mapping = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}

def extract_first_and_last_numbers(input_string):
    for key, value in number_mapping.items():
        input_string = input_string.replace(key, f'{key}{value}')

    numbers = re.findall(r'\d', input_string)

    first_number = numbers[0]
    last_number = numbers[-1]

    value = int(first_number + last_number)
    return value

sum = 0
calibration_numbers = []
for line in calibration_values:
    sum += extract_first_and_last_numbers(line)
    calibration_numbers.append(extract_first_and_last_numbers(line))

print(sum)
