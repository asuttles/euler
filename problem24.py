#
# A permutation is an ordered arrangement of objects.
# For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
#
# If all of the permutations are listed numerically or alphabetically,
# we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
#
# 012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the digits:
# 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
#
# ==============================================================================

# [[ [node], [branches] ]
#  [ [node], [branches] ]
#  ... ]

size = 10
tree = [[[],[i for i in range(size)]]]


# Convert a single Node and branch list to a
# node and list of branches for each branch of the node...
def nodeToBranches():

    node, branches = tree.pop(0)

    if len(branches) == 0:
        tree.insert(0,[node,branches])
        return False
    
    for i in range(len(branches)):
        thisBranch = branches[:]
        thisNode   = node[:]
        thisNode.append(thisBranch.pop(i))
        tree.append([thisNode, thisBranch])

    return True


# Reduce Each Node to a Node and Branches
while(nodeToBranches()):
    pass

# Delete empty branch lists ('y')
tree = [x for x,y in tree]


tree[999999]

# [2, 7, 8, 3, 9, 1, 5, 4, 6, 0]
        
