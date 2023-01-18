from functools import cmp_to_key

with open('day13.in', 'r') as file:
    data = file.read().split('\n\n')

# lambdas to be used in the function
I = lambda x: isinstance(x, int)
L = lambda x: isinstance(x, list)


# function to compare left and right
def cmp(l, r):
    # comparing integers
    if I(l) and I(r):
        if l < r:
            return -1
        return l > r
    # comparing lists
    if L(l) and L(r):
        for ii in range(min(len(l), len(r))):
            c = cmp(l[ii], r[ii])
            if c:
                return c
        return cmp(len(l), len(r))
    # comparing int and list
    if I(l) and L(r):
        return cmp([l], r)
    # comparing list and int
    if L(l) and I(r):
        return cmp(l, [r])


# init item storage
p = []
# initialise the sum
n = 0
for ii, ss in enumerate(data):
    # split up left and right values
    left, r = [eval(x) for x in ss.split()]
    if cmp(left, r) <= 0:
        n += ii + 1
    p.append(left)
    p.append(r)

p.append([[2]])
p.append([[6]])

p.sort(key=cmp_to_key(cmp))

print("Part 1: the sum is " + str(n))

print("Part 2: the decoder key for the distress signal is: " + str((p.index([[2]]) + 1) * (p.index([[6]]) + 1)))
