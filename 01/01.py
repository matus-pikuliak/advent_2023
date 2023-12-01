import string


def calibration(line):
    digits = [c for c in line if c in string.digits]
    return int(digits[0] + digits[-1])


txt = open('input').read()

print('#1', sum(map(calibration, txt.split())))

for i, name in enumerate('zero one two three four five six seven eight nine'.split()):
    txt = txt.replace(name, name + str(i) + name)

print('#2', sum(map(calibration, txt.split())))

