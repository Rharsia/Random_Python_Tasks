# problems = input("Enter your problems in a list format: ")
# problems = ["1 + 1", "2 - 1", "2022 - 1993", "15 + 15"]
problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49", "235 + 52"]

def arithmetic_arranger(problems, want_results = False):

    # create the output lines
    first_line = ""
    second_line = ""
    border_line = ""
    result_line = ""

    # max of 5 equations
    if len(problems) > 5:
        print("Too many problems.")
        exit()

    # split the individual equations
    splitted_equations = list()
    for eq in problems:
        splitted_equations.append(eq.split())

    # operator must be + or -
    for eq in splitted_equations:
        if eq[1] != "+" and eq[1] != "-":
            print("Operator must be '+' or '-'.")
            exit()

        # numbers must contain only digits
        if eq[0].isnumeric() and eq[2].isnumeric():
            filler = "why can't this be empty"
        else:
            print("Numbers must contain digist.")
            exit()

        # numbers cannot be more than 4 digits
        if len(eq[0]) > 4 or len(eq[2]) > 4:
            print("Numbers cannot be more than four digits")
            exit()


    # calculate the total length of individual equations
    for equation in splitted_equations:
        if len(equation[0]) > len(equation[2]):
            total_length = len(equation[0]) + 2
        else:
            total_length = len(equation[2]) + 2

        # get the result
        if equation[1] == "+":
            result = int(equation[0]) + int(equation[2])
        elif equation[1] == "-":
            result = int(equation[0]) - int(equation[2])


        # append to the first line
        first_line = first_line + "  " + ((total_length - len(equation[0])) * " ") + equation[0] + "  "

        # append to the second line
        second_line = second_line + "  " + equation[1] + ((total_length - len(equation[2]) - 1) * " ") + equation[2] + "  "

        # create the third line
        border_line = border_line + "  " + (total_length * "-") + "  "

        # create the result line
        result_line = result_line + "  " + ((total_length - len(str(result))) * " ") + str(result) + "  " 


    # print the results
    print(first_line)
    print(second_line)
    print(border_line)
    if want_results == True:
        print(result_line)
    
    # separate from next lines
    print()

arithmetic_arranger(problems)
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)