import re
from functools import lru_cache


@lru_cache
def options(row, lens):
    if len(lens) == 0:
        return row.count('#') == 0
    max_start = min((row+'#').index('#'), len(row) - sum(lens) - len(lens) + 1)
    return sum(
        options(row[start + lens[0] + 1:], tuple(lens[1:]))
        for start in range(max_start + 1)
        if row[start:start + lens[0]].count('.') == 0 and row[start + lens[0]] != '#'
    )


print(
    sum(
        options(
            line.split()[0]+'.',
            tuple(map(int, re.findall(r'\d+', line)))
        )
        for line in open('input')
    )
)

print(
    sum(
        options(
            '?'.join(line.split()[0] for _ in range(5))+'.',
            tuple(map(int, re.findall(r'\d+', line))) * 5
        )
        for line in open('input')
    )
)

