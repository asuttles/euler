gridSize = 20

topRow = [1] * (gridSize + 1)   # 1 path to each node along vert axis
othRow = [1] + [0] * gridSize   # 1 path to each node along horz axis
array = [topRow] + [othRow] * gridSize

# Num paths to each node is sum of paths to each parent node
for i in range(1, gridSize+1):  # Iter rows/columns
    for j in range(1, gridSize+1):
        # Sum paths to each parent node
        array[i][j] = array[i-1][j] + array[i][j-1]

print("There are {0} paths through"
      "a {1}x{1} grid".format(array[gridSize][gridSize], gridSize))
