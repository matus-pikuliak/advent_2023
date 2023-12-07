from collections import Counter

hands, vals = zip(*(line.split() for line in open('input')))
vals = list(map(int, vals))


def value1(hand):
    hand = [-'AKQJT98765432'.index(c) for c in hand]
    counts = Counter(hand).values()
    return sorted(counts, reverse=True), hand


def value2(hand):
    hand = [-'AKQT98765432J'.index(c) for c in hand]
    counts = sorted(Counter([n for n in hand if n < 12]).values(), reverse=True) + [0]
    counts[0] += hand.count(12)
    return sorted(counts, reverse=True), hand


for value in (value1, value2):
    print(sum(
        (i + 1) * val
        for i, (_, val) in enumerate(
            sorted((value(hand), val) for hand, val in zip(hands, vals)),
        )
    ))
