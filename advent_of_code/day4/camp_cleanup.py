file = open("C:/Users/42060/Desktop/Visual studio code lorekeep/Python projects/Advent_of_code/day4/input.txt", "r")

pairs = list()

for line in file:
    stripped_line = line.strip()
    pairs.append(stripped_line)

file.close()

pairs

pair = pairs[4]
pair

# get the pair separator
comma_index = pair.index(",")

first = pair[:comma_index]
second = pair[comma_index+1:]

first
second

# get the range separator and create the ranges
dash_index = first.index("-")
first_range = range(int(first[:dash_index]), int(first[dash_index+1:])+1)
first_range = list(first_range)
first_range

dash_index = second.index("-")
second_range = range(int(second[:dash_index]), int(second[dash_index+1:])+1)
second_range = list(second_range)
second_range

# check for full contaiments
full_contain = False
sum = 0
if len(first_range) >= len(second_range):
    for i in second_range:
        if i in first_range:
            sum += 1
    if sum == len(second_range):
        full_contain = True
elif len(first_range) < len(second_range):
    for i in first_range:
        if i in second_range:
            sum += 1
    if sum == len(first_range):
        full_contain = True
full_contain


# solution
answer = 0

for pair in pairs:
    comma_index = pair.index(",")

    first = pair[:comma_index]
    second = pair[comma_index+1:]

    dash_index = first.index("-")
    first_range = range(int(first[:dash_index]), int(first[dash_index+1:])+1)
    first_range = list(first_range)

    dash_index = second.index("-")
    second_range = range(int(second[:dash_index]), int(second[dash_index+1:])+1)
    second_range = list(second_range)

    full_contain = False
    sum = 0
    if len(first_range) >= len(second_range):
        for i in second_range:
            if i in first_range:
                sum += 1
        if sum == len(second_range):
            full_contain = True
    elif len(first_range) < len(second_range):
        for i in first_range:
            if i in second_range:
                sum += 1
        if sum == len(first_range):
            full_contain = True
    
    if full_contain == True:
        answer += 1

answer

# for pair in pairs:
#     comma_index = pair.index(",")

#     first = pair[:comma_index]
#     second = pair[comma_index+1:]

#     dash_index = first.index("-")
#     first_range = range(int(first[:dash_index]), int(first[dash_index+1:])+1)
#     first_range = list(first_range)

#     dash_index = second.index("-")
#     second_range = range(int(second[:dash_index]), int(second[dash_index+1:])+1)
#     second_range = list(second_range)

#     print(first)
#     print(second)
        
