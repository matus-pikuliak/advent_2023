import heapq

m = {
    (i, j): int(c)
    for i, line in enumerate(open('input'))
    for j, c in enumerate(line.strip())
}

cache = dict()
stack = [(0, 0, 0, 0, 0, 0, 0)]

part = 2

while stack:
    l, x, y, *dirs = heapq.heappop(stack)
    for i, (dx, dy) in enumerate(((0, 1), (1, 0), (0, -1), (-1, 0))):  # R D L U
        if dirs[(i + 2) % 4]:  # backward movement
            continue

        if part == 1 and dirs[i] == 3:  # fourth step
            continue
        if part == 2:
            if set(dirs) & {1, 2, 3} and dirs[i] == 0:  # locked-in movement
                continue
            if dirs[i] == 10:  # eleventh step
                continue

        nx, ny = x + dx, y + dy
        if (nx, ny) not in m:  # step outside
            continue
        nl = l + m[nx, ny]
        ndirs = tuple((j == i) * (d + 1) for j, d in enumerate(dirs))
        if cache.get((nx, ny, *ndirs), 1e50) <= nl:  # already in cache
            continue
        state = (nl, nx, ny, *ndirs)
        heapq.heappush(stack, (nl, nx, ny, *ndirs))
        cache[(nx, ny, *ndirs)] = nl

print(
    min(
        v
        for k, v in cache.items()
        if k[0] == 140 and k[1] == 140
    )
)
