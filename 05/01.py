import re
from itertools import chain

txt = open('input').read()


maps = [
    [
        list(map(int, line.split()))
        for line in lines.strip().split('\n')
    ]
    for lines in re.findall(r'\d[\d\s]+', txt)[1:]
]


def apply_map(val, m):
    for a, b, c in m:
        if b <= val < b + c:
            return a + val - b
    return val


def location(val):
    for m in maps:
        val = apply_map(val, m)
    return val


seeds = list(map(int, txt.split('\n')[0].split()[1:]))
print(min(map(location, seeds)))


def apply_map_range(start, end, m):
    c_start = start
    ranges = []
    while c_start <= end:
        for a, b, c in m:
            if b <= c_start < b + c:
                c_end = min(b + c - 1, end)
                ranges.append((a + c_start - b, a + c_end - b))
                break
        else:
            c_end = next((b for _, b, _ in m if c_start < b <= end), end)
            ranges.append((c_start, c_end))
        c_start = c_end + 1

    return ranges


ranges = [(a, a + b - 1) for a, b in zip(seeds[::2], seeds[1::2])]
for m in maps:
    ranges = list(chain.from_iterable(
        apply_map_range(start, end, m)
        for start, end in ranges
    ))
print(min(start for start, _ in ranges))