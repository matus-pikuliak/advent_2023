def rock_pos(col):
    pos = 0
    for i, tile in enumerate(col):
        if tile == '#':
            pos = i + 1
        if tile == 'O':
            yield pos
            pos += 1


def load(cols):
    return sum(
        sum(i + 1 for i, c in enumerate(col[::-1]) if c == 'O')
        for col in cols
    )


def move_col(col):
    rocks = set(rock_pos(col))
    return [
        {'#': '#'}.get(c, ('.', 'O')[i in rocks])
        for i, c in enumerate(col)
    ]


def cycle(cols):
    cols = [move_col(col) for col in cols]
    cols = [move_col(col) for col in zip(*cols)]
    cols = [move_col(col) for col in zip(*cols[::-1])]
    cols = [move_col(col) for col in zip(*cols[::-1])]
    return list(zip(*cols[::-1]))[::-1]


cols = list(zip(*open('input').read().splitlines()))

print(
    load(map(move_col, cols))
)

states = list()
cycles = 1000000000
for i in range(cycles):
    cols = cycle(cols)
    state = tuple(map(tuple, cols))
    if state in states:
        tail = states.index(state)
        print(load(states[tail + (cycles - tail - 1) % (len(states) - tail)]))
        break
    states.append(state)

