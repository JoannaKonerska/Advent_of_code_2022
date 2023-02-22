from collections import deque

Cubes = []
with open('day18.in', 'r') as file:
    for ll in file:
        Line = ll.strip()
        x, y, z = list(map(int, Line.split(",")))
        coord_tuple = (x, y, z)
        Cubes.append(coord_tuple)

CubesSet = set(Cubes)

AdjustedCoordinates = [(0, 0, 1), (0, 1, 0), (1, 0, 0), (0, 0, -1), (0, -1, 0), (-1, 0, 0)]

# init surface area
total_sa = 0
for x, y, z in Cubes:
    default_sa = 6
    for dx, dy, dz in AdjustedCoordinates:
        nx, ny, nz = x + dx, y + dy, z + dz
        # if there is the neighbour droplet
        if (nx, ny, nz) in CubesSet:
            default_sa -= 1
    total_sa += default_sa

print('Part 1: the total surface area is: ' + str(total_sa))

# let us figure out the boundaries
min_x, min_y, min_z = 50, 50, 50
max_x, max_y, max_z = 0, 0, 0
for x, y, z in Cubes:
    if x > max_x:
        max_x = x
    if x < min_x:
        min_x = x
    if y > max_y:
        max_y = y
    if y < min_y:
        min_y = y
    if z > max_z:
        max_z = z
    if z < min_z:
        min_z = z

# add the first boundary cube
Cube1 = (min_x - 1, min_y - 1, min_z - 1)
ExtCubes = []
ExtCubesSet = set()
ExtCubesSet.add(Cube1)

QueueCubes = deque()
QueueCubes.append(Cube1)
while QueueCubes:
    # get next cube in queue
    NextCube = QueueCubes.popleft()
    x, y, z = NextCube

    # add it as an external cube
    ExtCubes.append(NextCube)

    # test the "boundaries" of the cubes
    for dx, dy, dz in AdjustedCoordinates:
        nx, ny, nz = x + dx, y + dy, z + dz
        if nx < min_x - 1 or nx > max_x + 1 or ny < min_y - 1 or ny > max_y + 1 or nz < min_z - 1 or nz > max_z + 1:
            continue
        ThisCube = (nx, ny, nz)
        if ThisCube in CubesSet or ThisCube in ExtCubesSet:
            continue
        QueueCubes.append(ThisCube)
        ExtCubesSet.add(ThisCube)

# init total external surface area
total_ext_sa = 0
for x, y, z in ExtCubes:
    default_sa = 0
    for dx, dy, dz in AdjustedCoordinates:
        nx, ny, nz = x + dx, y + dy, z + dz
        # if there is a cube here
        if (nx, ny, nz) in CubesSet:
            default_sa += 1
    total_ext_sa += default_sa

print('Part 2: the total exterior surface area is: ' + str(total_ext_sa))
