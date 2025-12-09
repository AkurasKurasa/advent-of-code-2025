def conditions(x, y, matrix):
    totalRolls = 0
    rows = len(matrix)
    cols = len(matrix[0])

    # check top
    if (x - 1) >= 0 and matrix[x - 1][y] == "@":
        totalRolls += 1

    # check bottom
    if (x + 1) < rows and matrix[x + 1][y] == "@":
        totalRolls += 1

    # check left
    if (y - 1) >= 0 and matrix[x][y - 1] == "@":
        totalRolls += 1

    # check right
    if (y + 1) < cols and matrix[x][y + 1] == "@":
        totalRolls += 1

    # check top-left
    if (x - 1) >= 0 and (y - 1) >= 0 and matrix[x - 1][y - 1] == "@":
        totalRolls += 1

    # check top-right
    if (x - 1) >= 0 and (y + 1) < cols and matrix[x - 1][y + 1] == "@":
        totalRolls += 1

    # check bottom-left
    if (x + 1) < rows and (y - 1) >= 0 and matrix[x + 1][y - 1] == "@":
        totalRolls += 1

    # check bottom-right
    if (x + 1) < rows and (y + 1) < cols and matrix[x + 1][y + 1] == "@":
        totalRolls += 1

    return totalRolls < 4


matrix = [list(line.strip()) for line in open(r"day-4\given.txt")]

rolls = 0

for x in range(len(matrix)):
    for y in range(len(matrix[0])):
        if matrix[x][y] == "@" and conditions(x, y, matrix):
            matrix[x][y] = "."
            rolls += 1

print(rolls)


# Lengthy but fuck you