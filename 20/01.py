from itertools import count

flips = dict()
conjs = dict()

for line in open('input').read().splitlines():
    if not line.strip():
        continue
    i, o = line[1:].split(' -> ')
    if line[0] == '%':
        flips[i] = [False, o.split(', ')]
    elif line[0] == '&':
        conjs[i] = [{line[1:3]: False for line in open('input') if i+',' in line or i+'\n' in line}, o.split(', ')]
    else:
        broadcaster = o.split(', ')

stack = []
signals = list()


def do_flip(receiver, signal):
    if not signal:
        flips[receiver][0] = not flips[receiver][0]
        for comp in flips[receiver][1]:
            stack.append((receiver, comp, flips[receiver][0]))


def do_conj(sender, receiver, signal):
    conjs[receiver][0][sender] = signal
    out_signal = not all(conjs[receiver][0].values())
    for comp in conjs[receiver][1]:
        stack.append((receiver, comp, out_signal))


def do_broadcast(signal):
    signals.append(False)
    for comp in broadcaster:
        stack.append(('broadcaster', comp, signal))


def do_step():
    sender, receiver, signal = stack.pop(0)
    signals.append(signal)
    if receiver in flips:
        do_flip(receiver, signal)
    elif receiver in conjs:
        do_conj(sender, receiver, signal)
    else:
        pass


for i in count():
    do_broadcast(False)
    while stack:
        do_step()
    if i == 999:
        print(signals.count(True)*signals.count(False))
    if i == 5000:
        break


# Based on the reordered inputs
from math import lcm

print(
    lcm(
        0b111111101111,
        0b111101011011,
        0b111010110001,
        0b111111010001,
    )
)

