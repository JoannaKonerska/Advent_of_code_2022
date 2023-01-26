with open('day14.in', 'r') as file:
    data = file.read().strip()


# construct the cave layout first
# structure interpolation
def interpolate(start, end):
    x1, y1 = start
    x2, y2 = end

    # horizontal structure
    if x1 == x2:
        # horizontal line
        for y in range(min(y1, y2), max(y1, y2) + 1):
            yield x1, y

    # vertical structure
    if y1 == y2:
        # vertical line
        for x in range(min(x1, x2), max(x1, x2) + 1):
            yield x, y1


# parsing
def parse(data):
    grid = dict()
    bottom = 0

    for line in data.splitlines():
        # extract coords from each line
        coords = line.split(' -> ')
        # list of tuples of coordinates
        coords = [tuple(int(c) for c in coord.split(',')) for coord in coords]

        # go through each structure
        for start, end in zip(coords, coords[1:]):
            # get all the positions of the struct
            for pos in interpolate(start, end):
                grid[pos] = '#'
                if pos[1] > bottom:
                    # rising up the bottom due to struct
                    bottom = pos[1]

    return grid, bottom


# define what happens when sand drops
def drop_sand(grid, src, bottom):
    x, y = src

    while y < bottom:
        # implement stone drop logic
        for move in [(x, y + 1), (x - 1, y + 1), (x + 1, y + 1)]:
            # stay within grid
            if move not in grid:
                x, y = move
                break
        else:
            # return has stopped boolean and position
            return True, (x, y)

    return False, (x, y)


# Now we are ready to simulate the falling sand.
def part1(grid):
    grid, bottom = grid
    grid = grid.copy()

    src = (500, 0)
    cnt = 0

    while True:
        has_stopped, pos = drop_sand(grid, src, bottom)
        if not has_stopped:
            break
        # sand
        grid[pos] = 'o'
        cnt += 1

    return cnt


# There is no more abyss
def part2(grid):
    grid, bottom = grid

    src = (500, 0)
    cnt = 0

    while True:
        _, pos = drop_sand(grid, src, bottom + 1)
        # sand
        grid[pos] = 'o'
        cnt += 1
        if pos == src:
            break

    return cnt


print('Part 1: the units of sand to come to rest before sand starts flowing into the abyss is: '
      + str(part1(parse(data))))
print('Part 2: the units of sand to come to rest before sand starts flowing into the abyss is: ' +
      str(part2(parse(data))))
