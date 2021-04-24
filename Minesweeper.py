import random
grid = [[] for i in range(0, 8, 1)]
mask = [[] for i in range(0, 8, 1)]

def initialize_grid(grid):
    for row in grid:
        j = 0
        while (j < 8):
            row.append(0)
            j += 1
    return grid

def initialize_mask(mask):
    for row in mask:
        j = 0
        while (j < 8):
            row.append(0)
            j += 1
    return mask

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
            if (j == number_mines):
                row[j] = "mine"
            j += 1
    return grid

def find_ring(coordinates):
    ring = [[] for i in range(0, 8, 1)]
    for i in ring:
        i.append(-1)
        i.append(-1)
    
    if ((coordinates[0] - 1) < 0):
        ring[0][0] = "unavailable"
        ring[1][0] = ("unavailable")
        ring[2][0] = ("unavailable")
        if ((coordinates[1] - 1) < 0):
            ring[0][0] = ("unavailable")
            ring[3][0] = ("unavailable")
            ring[5][0] = ("unavailable")
        if ((coordinates[1] + 1) > 7):
            ring[2][0] = ("unavailable")
            ring[4][0] = ("unavailable")
            ring[7][0] = ("unavailable")
    elif ((coordinates[0] + 1) > 7):
        ring[5][0] = ("unavailable")
        ring[6][0] = ("unavailable")
        ring[7][0] = ("unavailable")
        if ((coordinates[1] - 1) < 0):
            ring[0][0] = ("unavailable")
            ring[3][0] = ("unavailable")
            ring[5][0] = ("unavailable")
        if ((coordinates[1] + 1) > 7):
            ring[2][0] = ("unavailable")
            ring[4][0] = ("unavailable")
            ring[7][0] = ("unavailable")
    elif ((coordinates[1] - 1) < 0):
        ring[0][0] = ("unavailable")
        ring[3][0] = ("unavailable")
        ring[5][0] = ("unavailable")
        if ((coordinates[0] - 1) < 0):
            ring[0][0] = ("unavailable")
            ring[1][0] = ("unavailable")
            ring[2][0] = ("unavailable")
        if ((coordinates[0] + 1) > 7):
            ring[5][0] = ("unavailable")
            ring[6][0] = ("unavailable")
            ring[7][0] = ("unavailable")
    elif ((coordinates[1] + 1) > 7):
        ring[2][0] = ("unavailable")
        ring[4][0] = ("unavailable")
        ring[7][0] = ("unavailable")
        if ((coordinates[0] - 1) < 0):
            ring[0][0] = ("unavailable")
            ring[1][0] = ("unavailable")
            ring[2][0] = ("unavailable")
        if ((coordinates[0] + 1) > 7):
            ring[5][0] = ("unavailable")
            ring[6][0] = ("unavailable")
            ring[7][0] = ("unavailable")

    i = 0
    while (i < 8):
        if (ring[i][0] != "unavailable"):
            if (i < 3):
               ring[i][0] = coordinates[0] - 1
            elif ((i == 3) or (i == 4)):
                ring[i][0] = coordinates[0]
            else:
                ring[i][0] = coordinates[0] + 1
        i += 1

    i = 0
    while (i < 8):
        if (ring[i][0] != "unavailable"):
            if ((i == 0) or (i == 3) or (i == 5)):
               ring[i][1] = coordinates[1] - 1
            elif ((i == 1) or (i == 6)):
                ring[i][1] = coordinates[1]
            else:
                ring[i][1] = coordinates[1] + 1
        i += 1
    return ring

def fill_numbers(grid):
    x = 0
    for row in grid:
        y = 0 
        for j in row:
            if (j == "mine"):
                #print([x, y])
                ring = find_ring([x, y])
                #print(ring)
                for num in ring:
                    if ((num[0] != "unavailable") and (grid[num[0]][num[1]] != "mine")):
                        grid[num[0]][num[1]] += 1
            y += 1
        x += 1
    return grid

#def format_grid(grid):
    #for row in grid:
        #for j in row:
            #if (j == 0):
                #j = ""
    #return grid

def count_grid(grid):
    count = 0
    for row in grid:
        for j in row:
            if (j != "mine"):
                count += 1
    return count

flag = 0
counter = 0
grid = initialize_grid(grid)
#print(grid)
grid = fill_grid(grid)
#print(grid)
grid = fill_numbers(grid)
#print(grid)
#grid = format_grid(grid)
#print(grid)
number = count_grid(grid)
num = 0
mask = initialize_mask(mask)
mask = fill_mask(mask)
number_tries = 50
while ((flag == 0) and (counter < number_tries)):
    for row in mask:
        print("- - - - - - - -")
        print("|" + str(row[0]) + "|" + " |" + str(row[1]) + "|"  + " |" + str(row[2]) + "|"  + " |" + str(row[3]) + "|"  + " |" + str(row[4]) + "|"  + " |" + str(row[5]) + "|"  + " |" + str(row[6]) + "|"  + " |" + str(row[7]) + "|")
        #print("\n")
        print("_ _ _ _ _ _ _ _")
    print("\n")
    x_coordinate = input('Insert the x coordinate: ')
    print("\n")
    y_coordinate = input('Insert the y coordinate: ')
    print("\n")
    x_coordinate = (int)(x_coordinate)
    y_coordinate = (int)(y_coordinate)
    if ((x_coordinate < 8) and (y_coordinate < 8)):
        mask[x_coordinate][y_coordinate] = grid[x_coordinate][y_coordinate]
    
    if (mask[x_coordinate][y_coordinate] != "mine"):
        num += 1
    else:
        counter = number_tries
        
    if (num == number):
        flag = 1
    
    counter += 1

if (counter == number_tries):
    print("You lost")
else:
    print("You won")
