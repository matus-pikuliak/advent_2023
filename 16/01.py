V = True
H = False

m = {
    i + j * 1j: c
    for i, line in enumerate(open('input'))
    for j, c in enumerate(line.strip())
}


def energize(*start):
    stack = [start]
    done = set()

    def maybe_add(a, b):
        if b in m and (a, b) not in done:
            stack.append((a, b))

    while stack:
        a, b = stack.pop()
        d = b - a
        done.add((a, b))
        c = m[b]
        if c == '.':
            maybe_add(b, b + d)
        if c == '|':
            maybe_add(b, b - 1)
            maybe_add(b, b + 1)
        if c == '-':
            maybe_add(b, b - 1j)
            maybe_add(b, b + 1j)
        if c == '\\':
            maybe_add(b, b + d.imag + 1j * d.real)
        if c == '/':
            maybe_add(b, b - d.imag - 1j * d.real)

    return len(set(b for _, b in done))


print(energize(-1j, 0))

print(
    max(
        max(energize(x - 1j, x) for x in range(110)),
        max(energize(x + 110j, x + 109j) for x in range(110)),
        max(energize(-1 + 1j * x, 1j * x) for x in range(110)),
        max(energize(110 + 1j * x, 109 + 1j * x) for x in range(110)),
    )
)