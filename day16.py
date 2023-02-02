import collections as c
import itertools
import re
import functools

r = r'Valve (\w+) .*=(\d*); .* valves? (.*)'

V, F, D = set(), dict(), c.defaultdict(lambda: 1000)

for v, f, us, in re.findall(r, open('day16.in').read()):
    # store node here
    V.add(v)
    # store flow here
    if f != '0':
        F[v] = int(f)
    for u in us.split(', '):
        D[u, v] = 1

for k, i, j in itertools.product(V, V, V):
    D[i, j] = min(D[i, j], D[i, k] + D[k, j])


@functools.cache
def search(t, u='AA', vs=frozenset(F), e=False):
    tt = max([F[v] * (t - D[u, v] - 1) + search(t - D[u, v] - 1, v, vs - {v}, e)
    for v in vs if D[u, v] < t] + [search(26, vs=vs) if e else 0])
    return tt


print('Part 1: the most pressure you can release is: ' + str(search(30)))
print('Part 2: the most pressure you and the elephant can release is: ' + str(search(26, e=True)))

