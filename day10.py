with open('day10.in', 'r') as file:
    data = file.read().strip().split('\n')

# initializing x
x = 1
# store the progress
x_list = [x]
# go line by line
for line in data:
    # if we are told to add
    if "add" in line:
        # add two current x
        x_list.extend([x, x])
        # add onto x
        x += int(line[5:])
    # if we are not adding
    else:
        x_list.append(x)

signal_strength = sum(x_list[cycle] * cycle for cycle in range(20, len(x_list), 40))

print("The sum of the signal strengths is: " + str(signal_strength))

# go over the rows
for yy in range(6):
    crt_line = ''
    # go over the columns
    for xx in range(40):
        cycle = xx + yy * 40
        crt_line += '.' if abs(xx - x_list[cycle + 1]) <= 1 else ' '
    print(crt_line)
