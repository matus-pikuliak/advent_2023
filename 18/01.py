lines = [
    line.split()
    for line in open('input')
]

x, y = 0, 0
verticals = []
horizontals = []

part1 = True
for d, l, code in lines:
    if part1:
        l = int(l)
    else:
        l = int(code[2:7], base=16)
        d = 'RDLU'[int(code[7])]
    if d == 'U':
        horizontals.append((x, y, y := y + l))
    if d == 'D':
        horizontals.append((x, y, y := y - l))
    if d == 'L':
        verticals.append((x, x := x + l, y))
    if d == 'R':
        verticals.append((x, x := x - l, y))


def es_shape(x, y1, y2):
    v1 = next(v for v in verticals if x in v[:2] and v[2] == y1)
    v2 = next(v for v in verticals if x in v[:2] and v[2] == y2)
    return (v1[0] + v1[1] - x > x) != (v2[0] + v2[1] - x > x)


def vol(x):
    ys = sorted(v[2] for v in verticals if min(v[0], v[1]) <= x <= max(v[0], v[1]))
    if not ys:
        return 0
    vol = 1
    next_on = True
    for y1, y2 in zip(ys, ys[1:]):
        if ((x, y1, y2) not in horizontals) and ((x, y2, y1) not in horizontals):
            if next_on:
                vol += y2 - y1 - 1
            next_on = not next_on
        else:
            vol += y2 - y1 - 1
            if not es_shape(x, y1, y2) and not es_shape(x, y2, y1):
                next_on = not next_on
        vol += 1
    return vol


xs = sorted(set(v[0] for v in verticals))
volume = 0
for (bottom, top) in zip(xs, xs[1:]):
    volume += vol(bottom)
    volume += (top - bottom - 1) * vol(bottom + 1)
volume += vol(top)

print(volume)
