def all_calories():
    file = open("C:/Users/42060/Documents/GitHub/Random_Python_Tasks/advent_of_code/day1/input file.txt", "r")

    calories = list()

    for line in file:
        stripped_line = line.strip()
        calories.append(stripped_line)

    file.close()

    all_calories = list()
    individual_calories0 = list()

    list_index = 0

    for i in calories:

        if i == "":
            exec(f"all_calories.append(individual_calories{list_index})")
            list_index += 1
            exec(f"individual_calories{list_index} = list()")
        elif i != "":
            i = int(i)
            exec(f"individual_calories{list_index}.append(i)")

    most = 0
    second = 0
    third = 0

    for i in range(len(all_calories)):
        if sum(all_calories[i]) > most:
            second = most
            most = sum(all_calories[i])
        elif sum(all_calories[i]) < most and sum(all_calories[i]) > second:
            third = second
            second = sum(all_calories[i])
        elif sum(all_calories[i]) < second and sum(all_calories[i]) > third:
            third = sum(all_calories[i])

    sorted_calories = [most, second, third]
    return sorted_calories[0]

all_calories()