from functools import cache
import re

lines = open('input').readlines()


def match(line):
    nums = re.findall(r'\d+', line)[1:]
    return len(nums) - len(set(nums))


print(
    sum(
        int(2 ** (match(line) - 1))
        for line in lines
    )
)


# Part 2 version 1
@cache
def f(i):
    if i >= len(lines):
        return 0
    return 1 + sum(f(j) for j in range(i + 1, i + match(lines[i]) + 1))

print(sum(f(i) for i in range(len(lines))))


# Part 2 version 2
cards = [1 for _ in range(201)]
for i, line in enumerate(lines):
    for j in range(match(line)):
        try:
            cards[i + j + 1] += cards[i]
        except IndexError:
            pass

print(sum(cards))
