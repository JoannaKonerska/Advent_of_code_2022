def make_moves(move, rope_len):
    # initialize
    xs = [0] * rope_len
    ys = [0] * rope_len
    visited = {(xs[-1], ys[-1])}

    # go through all the moves and record visited spaces
    for (mx, my), distance in move:
        for _ in range(distance):
            # make moves on x and y
            xs[0] += mx
            ys[0] += my
            for ii in range(rope_len - 1):
                # distance created with move
                dx = xs[ii + 1] - xs[ii]
                dy = ys[ii + 1] - ys[ii]
                if abs(dx) == 2 or abs(dy) == 2:
                    xs[ii + 1] = xs[ii] + int(dx / 2)
                    ys[ii + 1] = ys[ii] + int(dy / 2)
            # add on the visited spot
            visited.add((xs[-1], ys[-1]))

    # return the number of visited spot
    return len(visited)


# define the directions
dirs = {'L': (-1, 0), 'R': (1, 0), 'D': (0, -1), 'U': (0, 1)}

# define the moves
moves = [(dirs[line[0]], int(line[1:])) for line in open('day9.in')]

# print results
print("Part 1: the number of positions the tail visited is: " + str(make_moves(moves, 2)))
print("Part 2: the number of positions the tail visited is: " + str(make_moves(moves, 10)))
