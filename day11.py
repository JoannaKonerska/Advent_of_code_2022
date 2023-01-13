import re

# download the data
with open("day11.in", 'r') as file:
    data = file.read().strip().split('\n\n')

# define monkey behaviours
start_items = {}
operation = {}
div_test = {}
div_test_true = {}
div_test_false = {}
n_handle_items = {}

# loop through monkey data and populate
# monkey number init
m_number = 0
# division booster value
modd = 1
for monkey in data:
    monkey_data = monkey.split('\n')
    # number of handled items init
    n_handle_items[m_number] = 0
    for mdata in monkey_data:
        # operation
        if 'Operation' in mdata:
            operation[m_number] = mdata[23:]
        # starting item
        elif 'Starting' in mdata:
            start_items[m_number] = re.findall(r'\d+', mdata)
        # division test
        elif 'Test' in mdata:
            div_test[m_number] = int(re.findall(r'\d+', mdata)[0])
        # if test pass
        elif 'true' in mdata:
            div_test_true[m_number] = int(re.findall(r'\d+', mdata)[0])
        # if test fail
        elif 'false' in mdata:
            div_test_false[m_number] = int(re.findall(r'\d+', mdata)[0])
    # counts up monkey numbers
    modd *= div_test[m_number]
    m_number += 1


# process the rounds and compute monkey business
# number of rounds
n_round = 10000
# store the live items updates here
live_items = start_items
# for each round
for ii in range(n_round):
    # go through each monkey and get its info
    for mm in range(m_number):
        # monkey worry operations
        worry_op = operation[mm]
        # value for division test
        div_test_val = div_test[mm]
        # value for division test true
        div_test_true_val = div_test_true[mm]
        # value for division test fail
        div_test_false_val = div_test_false[mm]
        # compute new worry due to monkey, by going through the worry each monkey has
        for tt in live_items[mm]:
            # +int
            if '+' in worry_op and 'old' not in worry_op:
                tt_new = int(tt) + int(re.findall(r'\d+', worry_op)[0])
            elif '+' in worry_op and 'old' in worry_op:
                tt_new = int(tt) * 2
            elif '*' in worry_op and 'old' not in worry_op:
                tt_new = int(tt) * int(re.findall(r'\d+', worry_op)[0])
            elif '*' in worry_op and 'old' in worry_op:
                tt_new = int(tt) ** 2
            # monkey has stopped playing
            # tt_new //= 3 - only relevant for part 1
            # for part 2 only
            tt_new %= modd
            # where will monkey throw?
            if tt_new % div_test_val == 0:
                live_items[div_test_true_val].append(tt_new)
            else:
                live_items[div_test_false_val].append(tt_new)
            # update n handled items and empty monkey's hand
            n_handle_items[mm] += len(live_items[mm])
            live_items[mm] = []

# Get the monkey business
n_handles = list(n_handle_items.values())
n1 = max(n_handles)
n_handles.remove(n1)
n2 = max(n_handles)
monkey_business = n1 * n2
print("Part 2: Monkey business after 20 rounds is: " + str(monkey_business))
