import string
from collections import defaultdict
from itertools import takewhile, count, product
from math import prod

chars = {
    i + j * 1j: c
    for i, line in enumerate(open('input'))
    for j, c in enumerate(line.strip())
    if c != '.'
}


def is_digit(k):
    return chars.get(k, '.').isdigit()


def numbers():
    for k in chars:
        if is_digit(k) and not is_digit(k - 1j):
            yield list(takewhile(lambda x: is_digit(x), count(k, 1j)))


def value(num):
    return int(''.join(chars[k] for k in num))


def neigh(num):
    return {
        k + i + j: chars.get(k + i + j, '.')
        for k, i, j in product(num, [-1, 0, 1], [-1j, 0, 1j])
    }


print(
    sum(
        value(num)
        for num in numbers()
        if set(neigh(num).values()) - set(string.digits + '.')
    )
)


gears = defaultdict(lambda: list())
for num in numbers():
    for k, v in neigh(num).items():
        if v == '*':
            gears[k].append(value(num))

print(
    sum(
        prod(x)
        for x in gears.values()
        if len(x) == 2
    )
)