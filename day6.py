f = open('day6input.txt')

lights = [[False for j in range(1000)] for i in range(1000)]
lit_count = 0

for line in iter(f):
    split = line.split(" ")
    operation = split[0]
    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0
    if operation == "turn":
        operation += split[1]
        xy = split[2].split(",")
        x1 = int(xy[0])
        y1 = int(xy[1])
        xy = split[4].split(",")
        x2 = int(xy[0]) + 1
        y2 = int(xy[1]) + 1
    else:
        xy = split[1].split(",")
        x1 = int(xy[0])
        y1 = int(xy[1])
        xy = split[3].split(",")
        x2 = int(xy[0]) + 1
        y2 = int(xy[1]) + 1

    if operation == "turnon":
        for i in range(x1, x2):
            for j in range(y1, y2):
                lights[i][j] = True

    if operation == "turnoff":
        for i in range(x1, x2):
            for j in range(y1, y2):
                lights[i][j] = False

    if operation == "toggle":
        for i in range(x1, x2):
            for j in range(y1, y2):
                lights[i][j] = not lights[i][j]

for i in range(0, 1000):
    for j in range(0, 1000):
        if lights[i][j]:
            lit_count += 1

print(lit_count)
f.close()

f = open('day6input.txt')

lights1 = [[0 for j in range(1000)] for i in range(1000)]
brightness_count = 0

for line in iter(f):
    split = line.split(" ")
    operation = split[0]
    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0
    if operation == "turn":
        operation += split[1]
        xy = split[2].split(",")
        x1 = int(xy[0])
        y1 = int(xy[1])
        xy = split[4].split(",")
        x2 = int(xy[0]) + 1
        y2 = int(xy[1]) + 1
    else:
        xy = split[1].split(",")
        x1 = int(xy[0])
        y1 = int(xy[1])
        xy = split[3].split(",")
        x2 = int(xy[0]) + 1
        y2 = int(xy[1]) + 1

    if operation == "turnon":
        for i in range(x1, x2):
            for j in range(y1, y2):
                lights1[i][j] += 1

    if operation == "turnoff":
        for i in range(x1, x2):
            for j in range(y1, y2):
                if (lights1[i][j] - 1) <= 0:
                    lights1[i][j] = 0
                else:
                    lights1[i][j] -= 1

    if operation == "toggle":
        for i in range(x1, x2):
            for j in range(y1, y2):
                lights1[i][j] += 2

for i in range(0, 1000):
    for j in range(0, 1000):
        if lights1[i][j]:
            brightness_count += lights1[i][j]

print(brightness_count)
f.close()