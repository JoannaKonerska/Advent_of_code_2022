import numpy as np

# put input file as matrix format

grid = np.array([list(x.strip()) for x in open("day8.in")], int)

# get number of rows and columns
nrow, ncol = np.shape(grid)

# initializing the best view score
best_view_score = 1
# initializing visible trees on the edge
number_of_visible_trees = ncol * 2 + (nrow - 2) * 2
# go through all the rows inside
for ii in range(1, nrow - 1):
    # go through all the columns onside
    for iii in range(1, ncol - 1):
        # tree of interest
        tree = grid[ii, iii]
        tree_up = grid[:ii, iii]
        tree_down = grid[ii + 1:, iii]
        tree_right = grid[ii, iii + 1:]
        tree_left = grid[ii, :iii]

        # compute the tallest tree in each direction
        tallest_tree_up = max(tree_up)
        tallest_tree_down = max(tree_down)
        tallest_tree_right = max(tree_right)
        tallest_tree_left = max(tree_left)

        # count the number of trees visible looking up
        count_visible_tree_up = 0
        for tt in range(len(tree_up)):
            count_visible_tree_up += 1
            if tree_up[len(tree_up) - 1 - tt] >= tree:
                break

        # count the number of trees visible looking down
        count_visible_tree_down = 0
        for tt in range(len(tree_down)):
            count_visible_tree_down += 1
            if tree_down[tt] >= tree:
                break

        # count the number of trees visible looking right
        count_visible_tree_right = 0
        for tt in range(len(tree_right)):
            count_visible_tree_right += 1
            if tree_right[tt] >= tree:
                break

        # count the number of trees visible looking left
        count_visible_tree_left = 0
        for tt in range(len(tree_left)):
            count_visible_tree_left += 1
            if tree_left[len(tree_left) - 1 - tt] >= tree:
                break

        # if the tree is taller than the maxes in any direction see the tree
        if tree > tallest_tree_up or tree > tallest_tree_down or tree > tallest_tree_right or tree > tallest_tree_left:
            number_of_visible_trees += 1

        # if the view score is highier we overwrite the best score
        view_score = count_visible_tree_up * count_visible_tree_down * count_visible_tree_left * count_visible_tree_right
        if view_score > best_view_score:
            best_view_score = view_score

print(" Answer to the part 1 is: Number of visible trees: " + str(number_of_visible_trees))
print(" Answer to pert 2 is: The best view score is " + str(best_view_score))
