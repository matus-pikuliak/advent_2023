from copy import copy
from math import prod
from operator import lt, gt


def apply_rules(rules, xmas):
    for rule in rules[:-1]:
        if (lt, gt)[rule[1] == '>'](xmas[rule[0]], int(rule[2:rule.index(':')])):
            return rule.split(':')[1]
    return rules[-1]

mapping = dict()
rules, xmases = open('input').read().split('\n\n')
for line in rules.split('\n'):
    name, rest = line.split('{')
    rules = rest[:-1].split(',')
    mapping[name] = rules

sm = 0
for line in xmases.split('\n'):
    xmas = {val[0]: int(val[2:]) for val in line[1:-1].split(',')}
    state = 'in'
    while state not in 'AR':
        state = apply_rules(mapping[state], xmas)
    if state == 'A':
        sm += sum(xmas.values())
print(sm)


def combine_bounds(bounds, new_bound, c):
    bounds = copy(bounds)
    new_bound = (max(new_bound[0], bounds[c][0]), min(new_bound[1], bounds[c][1]))
    bounds[c] = new_bound
    return bounds


def bound_volume(bounds):
    if any(mn > mx for mn, mx in bounds.values()):
        return 0
    return prod(mx - mn + 1 for mn, mx in bounds.values())


def num_accept(rules, bounds):
    sm = 0
    for rule in rules[:-1]:
        xmas = rule[0]
        num = int(rule.split(':')[0][2:])
        state = rule.split(':')[1]

        if rule[1] == '>':
            acc, ref = (num+1, 4000), (1, num)
        else:
            acc, ref = (1, num-1), (num, 4000)

        if state == 'A':
            sm += bound_volume(combine_bounds(bounds, acc, xmas))
        elif state == 'R':
            pass
        else:
            sm += num_accept(mapping[state], combine_bounds(bounds, acc, xmas))

        bounds = combine_bounds(bounds, ref, xmas)

    if rules[-1] == 'A':
        sm += bound_volume(bounds)
    elif rules[-1] == 'R':
        pass
    else:
        sm += num_accept(mapping[rules[-1]], bounds)
    return sm


print(num_accept(mapping['in'], {c: (1, 4000) for c in 'xmas'}))
