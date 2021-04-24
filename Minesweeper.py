#!/usr/bin/python
alias python = 'winpty python.exe'
import random
grid = [[] for i in range(0, 8, 1)]
mask = [[] for i in range(0, 8, 1)]

def fill_mask(mask):
    for row in mask:
        j = 0
        while (j < 8):
            row[j] = ""
            j += 1
    return mask

def fill_grid(grid):
    for row in grid:
        number_mines = random.randint(0, 7)
        j = 0
        while (j < 8):
            if (j != number_mines):
                row[j] = 0
            else:
                row[j] = "mine"
            j += 1
    return grid

def find_ring(coordinates):
    ring = [[] for i in range(0, 8, 1)]
    if ((coordinates[0] - 1) < 0):
        ring[0].append("unavailable")
        ring[1].append("unavailable")
        ring[2].append("unavailable")
        if ((coordinates[1] - 1) < 0):
            ring[0].append("unavailable")
            ring[3].append("unavailable")
            ring[5].append("unavailable")
        if ((coordinates[1] + 1) > 7):
            ring[2].append("unavailable")
            ring[4].append("unavailable")
            ring[7].append("unavailable")
    elif ((coordinates[0] + 1) > 7):
        ring[5].append("unavailable")
        ring[6].append("unavailable")
        ring[7].append("unavailable")
        if ((coordinates[1] - 1) < 0):
            ring[0].append("unavailable")
            ring[3].append("unavailable")
            ring[5].append("unavailable")
        if ((coordinates[1] + 1) > 7):
            ring[2].append("unavailable")
            ring[4].append("unavailable")
            ring[7].append("unavailable")
    elif ((coordinates[1] - 1) < 0):
        ring[0].append("unavailable")
        ring[3].append("unavailable")
        ring[5].append("unavailable")
        if ((coordinates[0] - 1) < 0):
            ring[0].append("unavailable")
            ring[1].append("unavailable")
            ring[2].append("unavailable")
        if ((coordinates[0] + 1) > 7):
            ring[5].append("unavailable")
            ring[6].append("unavailable")
            ring[7].append("unavailable")
    elif ((coordinates[1] + 1) > 7):
        ring[2].append("unavailable")
        ring[4].append("unavailable")
        ring[7].append("unavailable")
        if ((coordinates[0] - 1) < 0):
            ring[0].append("unavailable")
            ring[1].append("unavailable")
            ring[2].append("unavailable")
        if ((coordinates[0] + 1) > 7):
            ring[5].append("unavailable")
            ring[6].append("unavailable")
            ring[7].append("unavailable")

    i = 0
    while (i < 8)
        if (ring[i][0] != "unavailable"):
            if (i < 3):
               ring[i][0] = coordinates[0] - 1
            elif ((i == 3) or (i == 4)):
                ring[i][0] = coordinates[0]
            else:
                ring[i][0] = coordinates[0] + 1

    i = 0
    while (i < 8)
        if (ring[i][0] != "unavailable"):
            if ((i == 0) or (i == 3) or (i == 5)):
               ring[i][1] = coordinates[1] - 1
            elif ((i == 1) or (i == 6)):
                ring[i][1] = coordinates[1]
            else:
                ring[i][1] = coordinates[1] + 1
    return ring

def fill_numbers(grid):
    x = 0
    for row in grid:
        y = 0 
        for j in row:
            if (j == "mine"):
                ring = find_ring(x, y)
                for num in ring:
                    if (num[0] != "unavailable"):
                        grid[num[0]][num[1]] += 1
            y += 1
        x += 1
    return grid

def format_grid(grid):
    for row in grid:
        for j in row:
            if (j == 0):
                j = ""
    return grid

def count_grid(grid):
    count = 0
    for row in grid:
        for j in row:
            if (j != "mine"):
                count += 1
    return count

flag = 0
counter = 0
while ((flag == 0) and (counter < 3)):
    grid = fill(grid)
    grid = fill_numbers(grid)
    grid = format_grid(grid)
    number = count_grid(grid)
    num = 0
    mask = fill(mask)
    for row in mask:
        print("-- -- -- -- -- -- -- --\n")
        for value in row:
            print("|value|")
        print("\n")
        print("_ _ _ _ _ _ _ _\n")
    x_coordinate = input('Insert the x coordinate: ')
    y_coordinate = input('Insert the y coordinate: ')
    mask[x_coordinate][y_coordinate] = grid[x_coordinate][y_coordinate]
    if (mask[x_coordinate][y_coordinate] != "mine"):
        num += 1
    if (num == number):
        flag = 1
    counter += 1

if (counter == 3):
    print("You lost")
else:
    print("You won")