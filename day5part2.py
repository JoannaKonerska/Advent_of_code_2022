# download the data

stack_load = [[' '], ['Q', 'W', 'P', 'S', 'Z', 'R', 'H', 'D'], ['V', 'B', 'R', 'W', 'Q', 'H', 'F'],
              ['C', 'V', 'S', 'H'], ['H', 'F', 'G'], ['P', 'G', 'J', 'B', 'Z'], ['Q', 'T', 'J', 'H', 'W', 'F', 'L'],
              ['Z', 'T', 'W', 'D', 'L', 'V', 'J', 'N'], ['D', 'T', 'Z', 'C', 'J', 'G', 'H', 'F'],
              ['W', 'P', 'V', 'M', 'B', 'H']]

with open("day5.in") as file:
    stack_strings, instructions = (i.splitlines() for i in file.read().strip("\n").split("\n\n"))

stacks = {int(digit): stack_load[int(digit)] for digit in stack_strings[-1].replace(" ", "")}
indexes = [index for index, char in enumerate(stack_strings[-1]) if char != " "]


def getstackends():
    answer = ""
    for stack in stacks:
        answer += stacks[stack][-1]
    return answer

# PART 2#


for instruction in instructions:
    instruction = instruction.replace("move ", "").replace("from ", "").replace("to ", "").strip().split(" ")
    instruction = [int(i) for i in instruction]

    crates = instruction[0]
    from_stack = instruction[1]
    to_stack = instruction[2]

    crates_to_remove = stacks[from_stack][-crates:]
    stacks[from_stack] = stacks[from_stack][:-crates]

    for crate in crates_to_remove:
        stacks[to_stack].append(crate)

print("Answer for part 2: ", getstackends())
