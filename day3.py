f = open('day3input.txt')
x = 0
y = 0
homes = set()

for char in f.readlines()[0]:
    if (x, y) not in homes:
        homes.add((x, y))

    if char == '<':
        x -= 1
    elif char == '>':
        x += 1
    elif char == '^':
        y += 1
    elif char == 'v':
        y -= 1

print(len(homes))
f.close()

f = open('day3input.txt')
homes_santa = set()
homes_robosanta = set()
sx = 0
sy = 0
rx = 0
ry = 0

for index, char in enumerate(f.readlines()[0]):
    x1 = 0
    y1 = 0

    if char == '<':
        x1 -= 1
    elif char == '>':
        x1 += 1
    elif char == '^':
        y1 += 1
    elif char == 'v':
        y1 -= 1

    if index % 2 == 0:
        rx += x1
        ry += y1
        homes_robosanta.add((rx, ry))
    else:
        sx += x1
        sy += y1
        homes_santa.add((sx, sy))

print(len(homes_robosanta | homes_santa))
f.close()