m = {
    i + 1j * j: c
    for i, line in enumerate(open('input'))
    for j, c in enumerate(line)
}

dirs = {
    ('|', -1): -1,
    ('|', 1): 1,
    ('-', 1j): 1j,
    ('-', -1j): -1j,
    ('L', 1): 1j,
    ('L', -1j): -1,
    ('J', 1): -1j,
    ('J', 1j): -1,
    ('7', -1): -1j,
    ('7', 1j): 1,
    ('F', -1): 1j,
    ('F', -1j): 1,
}

start = p = next(k for k, v in m.items() if v == 'S')
d = -1
points = [p]

while True:
    p += d
    if p == points[0]:
        break
    points.append(p)
    d = dirs[m[p], d]

print(len(points)//2)

points = [p * 2 for p in points]
gaps = [(a + b) / 2 for a, b in zip(points, points[1:] + [points[0]])]
points = set(points) | set(gaps)

for sp in points:
    if sp + 1 in points:
        continue

    gen = {sp + 1}
    flood = set()

    while gen:
        flood |= gen
        gen = (set(p + d for p in gen for d in [-1, 1, -1j, 1j]) - flood) - points
        if 0 in gen:
            break

    if 0 not in gen:
        print(
            sum(
                int(p.real) % 2 == 0 and int(p.imag) % 2 == 0
                for p in flood
            )
        )
        break

