rows = 5

for x in range(rows):
    for y in range(rows * 2 - 1):
        if (y == rows - 1 - x or y == rows * 2 - 2 - x or x == 0 or x == rows - 1) and y >= rows - 1 - x and y <= rows * 2 - 2 - x:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()