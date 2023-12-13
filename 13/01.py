def horizontal_mirror(rows):
    nums = [
        sum(
            (2 * (c == '#')) ** (i + 1)
            for i, c in enumerate(row)
        )
        for row in rows
    ]
    for x in range(len(nums) // 2, 0, -1):
        if nums[:x] == nums[x:2*x][::-1]:
            yield x


def value(rows):
    cols = [
        [
            rows[i][j]
            for i in range(len(rows))
        ]
        for j in range(len(rows[0]))
    ]
    for x in horizontal_mirror(cols):
        yield x
    for x in horizontal_mirror(cols[::-1]):
        yield len(cols) - x
    for x in horizontal_mirror(rows):
        yield x * 100
    for x in horizontal_mirror(rows[::-1]):
        yield (len(rows) - x) * 100


def fix_smudge(rows):
    rows = list(map(list, rows))
    og = next(value(rows))
    for i in range(len(rows)):
        for j in range(len(rows[0])):
            rows[i][j] = {'.': '#', '#': '.'}[rows[i][j]]
            if l := set(value(rows)) - {og}:
                return l.pop()
            rows[i][j] = {'.': '#', '#': '.'}[rows[i][j]]


print(
    sum(
        next(value(pattern.split('\n')))
        for pattern in open('input').read().strip().split('\n\n')
    )
)

print(
    sum(
        fix_smudge(pattern.split('\n'))
        for pattern in open('input').read().strip().split('\n\n')
    )
)
