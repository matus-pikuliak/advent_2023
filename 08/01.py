import re
from itertools import cycle

lines = open('input').read().splitlines()

nodes = dict()
for line in lines[2:]:
    a, b, c = re.findall(r'[0-9A-Z]{3}', line)
    nodes[a] = (b, c)

c = 'AAA'
for i, lr in enumerate(cycle(lines[0])):
    c = nodes[c][lr == 'R']
    if c == 'ZZZ':
        print(i + 1)
        break


def step_to_z(c):
    for i, lr in enumerate(cycle(lines[0])):
        c = nodes[c][lr == 'R']
        if c.endswith('Z'):
            return i + 1


cycles = [
    step_to_z(node)
    for node in nodes
    if node.endswith('A')
]


def gcp(x, y):
    while True:
        if y > x:
            x, y = y, x
        if y == 0:
            return x
        x, y = y, x - y


def lcm(x, y):
    return x * y // gcp(x, y)


l = cycles[0]
for c in cycles[1:]:
    l = lcm(l, c)

print(l)