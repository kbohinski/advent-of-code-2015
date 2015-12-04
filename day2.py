f = open('day2input.txt')
surface_area = 0
ribbon_len = 0

for line in iter(f):
    [l, w, h] = map(int, line.split("x"))
    low = min((l * w), (l * h), (w * h))
    surface_area += (((2 * l * w) + (2 * w * h) + (2 * h * l)) + low)
    bow = (l * w * h)
    low = (2 * min((w + h), (l + w), (l + h)))
    ribbon_len += (bow + low)

print("Wrapping Paper Needed: " + str(surface_area))
print("Ribbon Needed: " + str(ribbon_len))

f.close()