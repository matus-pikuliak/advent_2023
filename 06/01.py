import re
from math import prod

txt = """
Time:        48     93     85     95
Distance:   296   1928   1236   1391
"""

nums = list(map(int, re.findall(r'\d+', txt)))
times, distances = nums[:4], nums[4:]


def win_count(t, d):
    return sum(
        i * (t - i) > d
        for i in range(t)
    )


print(
    prod(
        win_count(t, d)
        for t, d in zip(times, distances)
    )
)

nums = list(map(int, re.findall(r'\d+', txt.replace(' ',''))))
print(win_count(*nums))
