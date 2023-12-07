file_path = '/Users/yichengzhang/Documents/GitHub/Random_Python_Tasks/advent_of_code/2023/day_2/input.txt'

with open(file_path, 'r') as file:
    games = [line.strip() for line in file.readlines()]

games

game_dict = {}

for game in games:
    parts = game.split(':')

    key = parts[0].strip()
    value = parts[1].strip()

    game_dict[key] = [value]

game_dict

for item in game_dict:
    print(item)
    print(game_dict[item])

first_game = game_dict['Game 1'][0]
first_game

sets = first_game.split(';')

sets_dict = {}

sets

first_pull = sets[0]
first_pull

cubes = first_pull.split(',')
cubes

for cube_color in cubes:
    cube = cube_color.split()
    print(cube)
