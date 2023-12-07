import pandas as pd

file_path = '/Users/yichengzhang/Documents/GitHub/Random_Python_Tasks/advent_of_code/2023/day_2/input.txt'

with open(file_path, 'r') as file:
    games = [line.strip() for line in file.readlines()]

games

games_df = pd.DataFrame()

for game in games:
    print(game)
    