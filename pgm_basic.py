# mousebot_game.py
# Experiment 1: Python Fundamentals through a MouseBot Navigation Game
# Author: MMJ | Course: Artificial Intelligence | Language: Python 3.x

map = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', '#', '#', ' ', '#', '#', ' ', '#'],
    ['#', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', '#'],
    ['#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#'],
    ['#', ' ', '#', '#', '#', ' ', '#', ' ', '#', '#'],
    ['#', 'S', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', '#', ' ', '#', '#', '#', '#', 'G', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
]

def display_map():
    for row in map:
        print(' '.join(row))

def find_position(symbol):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == symbol:
                return (i, j)
    return None

def game():
    mouse_pos = find_position('S')
    goal_pos = find_position('G')
    moves = 0

    while mouse_pos != goal_pos:
        display_map()
        move = input("Enter move (W/A/S/D) or Q to quit: ").upper()
        if move == 'Q':
            print("Game quit.")
            return
        new_pos = list(mouse_pos)

        if move == 'W':
            new_pos[0] -= 1
        elif move == 'S':
            new_pos[0] += 1
        elif move == 'A':
            new_pos[1] -= 1
        elif move == 'D':
            new_pos[1] += 1
        else:
            print("Invalid move! Use W/A/S/D.")
            continue

        if map[new_pos[0]][new_pos[1]] != '#':
            moves += 1
            map[mouse_pos[0]][mouse_pos[1]] = ' '
            mouse_pos = tuple(new_pos)
            map[mouse_pos[0]][mouse_pos[1]] = 'S'
        else:
            print("You hit a wall! Try a different move.")

    print("Congratulations! You've reached the goal!")
    print("Total moves: "+ str(moves))

game()