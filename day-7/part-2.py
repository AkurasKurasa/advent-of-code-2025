from functools import cache

grid = [list(line.strip()) for line in open(r"day-7\given.txt")]

S = [(r, c) for r, row in enumerate(grid) for c, char in enumerate(row) if char == "S"][0]

memory = {}

def possibility(r, c):
    if (r, c) in memory:
        return memory[(r, c)]

    if r > len(grid) - 1:
        return 1

    cell = grid[r][c]

    if cell == "." or cell == "S":
        result = possibility(r + 1, c)

    elif cell == "^":
        result = possibility(r, c - 1) + possibility(r, c + 1)

    else:
        result = 0

    memory[(r, c)] = result
    return result


print(possibility(S[0], S[1]))