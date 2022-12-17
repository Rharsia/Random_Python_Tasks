file = open("C:/Users/42060/Desktop/Visual studio code lorekeep/Python projects/Advent_of_code/day4/input.txt", "r")

pairs = list()

for line in file:
    stripped_line = line.strip()
    pairs.append(stripped_line)

file.close()

pairs

answer = 0

for pair in pairs:
    # get the pair separator
    comma_index = pair.index(",")

    first = pair[:comma_index]
    second = pair[comma_index+1:]

    # get the range separator and create the ranges
    dash_index = first.index("-")
    first_range = range(int(first[:dash_index]), int(first[dash_index+1:])+1)
    first_range = list(first_range)

    dash_index = second.index("-")
    second_range = range(int(second[:dash_index]), int(second[dash_index+1:])+1)
    second_range = list(second_range)

    # check for overlaps
    overlap = False
    
    for section in first_range:
        if section in second_range:
            overlap = True
    for section in second_range:
        if section in first_range:
            overlap = True

    if overlap == True:
        answer += 1

answer