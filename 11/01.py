from functools import lru_cache
from itertools import combinations

m = {
    (i + 1j * j)
    for i, line in enumerate(open('input'))
    for j, c in enumerate(line)
    if c == '#'
}


@lru_cache
def empty_row(i):
    return not any(x.real == i for x in m)


@lru_cache
def empty_col(i):
    return not any(x.imag == i for x in m)


def dist(p1, p2, factor):
    mn_real, mx_real = int(min(p1.real, p2.real)), int(max(p1.real, p2.real))
    mn_imag, mx_imag = int(min(p1.imag, p2.imag)), int(max(p1.imag, p2.imag))
    d = mx_real - mn_real + mx_imag - mn_imag + factor*sum(empty_row(i) for i in range(mn_real, mx_real)) + factor*sum(empty_col(i) for i in range(mn_imag, mx_imag))
    return d

print(
    sum(
        dist(p1, p2, factor=1)
        for p1, p2 in combinations(m, r=2)
    )
)
print(
    sum(
        dist(p1, p2, factor=999999)
        for p1, p2 in combinations(m, r=2)
    )
)