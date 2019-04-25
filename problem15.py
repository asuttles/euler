# Starting in the top left corner of a 2×2 grid,
# and only being able to move to the right and down,
# there are exactly 6 routes to the bottom right corner.
#
# How many such routes are there through a 20×20 grid?


# Note: This problem grows exponentially as gridSize grows
#       See 'alternate' solution for a combinatorial approach
gridSize = 5
numMoves = 0
positions = [(0, 0)]

while len(positions) > 0:
    row, col = positions.pop(0)

    # Finish Line
    if (row == gridSize) and (col == gridSize):
        numMoves += 1

    else:
        # Move Right
        if col < gridSize:
            positions.append((row, col+1))

        # Move Down
        if row < gridSize:
            positions.append((row+1, col))

print(
    "There are {0} paths through a {1}x{1} grid".format(numMoves, gridSize))
