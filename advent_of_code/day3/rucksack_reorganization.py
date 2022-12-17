file = open("C:/Users/42060/Documents/GitHub/Random_Python_Tasks/advent_of_code/day1/input file.txt", "r")

calories = list()

for line in file:
    stripped_line = line.strip()
    calories.append(stripped_line)

file.close()