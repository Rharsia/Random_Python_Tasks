def sums_of_calories():
    file = open("C:/Users/JanZh/OneDrive/Plocha/input file.txt", "r")

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

    sums_of_calories = list()
    for i in all_calories:
        sums_of_calories.append(sum(i))

    sums_of_calories = sorted(sums_of_calories, reverse=True)

    top_three = sorted(sums_of_calories(), reverse=True)[0:3]

    return sum(top_three)