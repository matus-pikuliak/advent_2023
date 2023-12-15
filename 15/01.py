def hash(s):
    v = 0
    for c in s:
        v += ord(c)
        v *= 17
        v %= 256
    return v

instructions = open('input').read().split(',')

print(
    sum(
        hash(s)
        for s in instructions
    )
)

boxes = [dict() for _ in range(256)]

for instruction in instructions:
    if '-' in instruction:
        label = instruction[:-1]
        box = boxes[hash(label)]
        if label in box:
            del box[label]
    else:
        label, num = instruction.split('=')
        boxes[hash(label)][label] = int(num)

print(
    sum(
        (i + 1) * (j + 1) * val
        for i, box in enumerate(boxes)
        for j, val in enumerate(box.values())
    )
)
