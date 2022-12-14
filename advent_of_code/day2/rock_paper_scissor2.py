def strategy_guide2():
    file = open("C:/Users/42060/Documents/GitHub/Random_Python_Tasks/advent_of_code/day2/input_file.txt", "r")

    moves = list()

    for line in file:
        stripped_line = line.strip()
        moves.append(stripped_line)

    file = file.close()

    # X = lose
    # Y = draw
    # Z = win

    score = 0

    for i in range(len(moves)):
        if moves[i][2] == "X":
            result = "loss"
        elif moves[i][2] == "Y":
            result = "draw"
            score += 3
        elif moves[i][2] == "Z":
            result = "win"
            score += 6

        if moves[i][0] == "B" and moves[i][2] == "X" or moves[i][0] == "A" and moves[i][2] == "Y" or moves[i][0] == "C" and moves[i][2] == "Z":
            play = "rock"
            score += 1
        elif moves[i][0] == "C" and moves[i][2] == "X" or moves[i][0] == "B" and moves[i][2] == "Y" or moves[i][0] == "A" and moves[i][2] == "Z":
            play = "paper"
            score += 2
        elif moves[i][0] == "A" and moves[i][2] == "X" or moves[i][0] == "C" and moves[i][2] == "Y" or moves[i][0] == "B" and moves[i][2] == "Z":
            play = "scissor"    
            score += 3

    return score

strategy_guide2()