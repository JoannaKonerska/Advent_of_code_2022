
# getting data
with open("day1.in") as file:
    data = [i for i in file.read().strip().split("\n")]

# print(data)

# stating my variables
max_value = 0
max2 = 0
max3 = 0
count = 0
# if statement counting the totals
for item in data:
    if item == '':
        count = 0
    else:
        num = int(item)
        count += num

    if count > max_value:
        max_value = count
    elif count > max2:
        max2 = count
    elif count > max3:
        max3 = count

print("Answer to part 1:", max_value)
print("Answer to part 2:", max_value+max2+max3)
