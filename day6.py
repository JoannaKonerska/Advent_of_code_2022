# download the data

with open("day6.in") as file:
    input_data = file.read()

# PART 1#

for i in range(4, len(input_data)):
    s = set(input_data[(i-4):i])
    if len(s) == 4:
        print("Answer to part 1: ", i)
        break

for i in range(14, len(input_data)):
    s = set(input_data[(i - 14):i])
    if len(s) == 14:
        print("Answer to part 2: ", i)
        break
