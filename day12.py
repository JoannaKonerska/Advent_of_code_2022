with open('day12.in', 'r') as file:
    data = file.read()


def can_go(g, p1, p2):
    return(p2 in g and
        ((g[p1] == 'E' and g[p2] in 'yz') or
            (g[p2] == 'S' and g[p1] in 'ab') or
            (g[p2] != "S" and g[p1] != "E" and ord(g[p1]) - ord(g[p2]) <= 1)))


# defining grid
grid = {x + y * 1j: h for y, line in enumerate(data.split('\n'))
        for x, h in enumerate(line)}

# find the starting and ending position
start = [p for p, h in grid.items() if h == 'S'][0]
end = [p for p, h in grid.items() if h == 'E'][0]

# starting from the 'end' find distances to get to 'start'
# init dist dict from end
distance = {end: 0}
# init place we can get to
queue = [end]
# keep walking around as long as we can get somewhere
while queue:
    p1 = queue.pop(0)
    # we are here
    # options around us
    for p2 in [p1 - 1, p1 + 1, p1 + 1j, p1 - 1j]:
        # if we haven't been here before, and we can get there
        if p2 not in distance and can_go(grid, p1, p2):
            # record distance from the end
            distance[p2] = distance[p1] + 1
            # add it to our places to go
            queue.append(p2)

# Part 2 - find the position in distance for S or any a
short_dist = sorted(distance[p] for p in distance if grid[p] in "Sa")[0]

print('Part 1: the shortest distance from the start to the end is: ' + str(distance[start]))
print('Part 2: the shortest distance from the start to the end is: ' + str(short_dist))
