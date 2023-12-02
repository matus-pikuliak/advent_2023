import re
from math import prod


def f(line, c):
    return max(map(int, re.findall(fr'(\d+) {c}', line)))


print(
    sum(
        prod(f(line, c) for c in ['red', 'green', 'blue'])
        for line in open('input')
    )
)
