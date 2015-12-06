f = open('day5input.txt')
nice_count = 0

for line in iter(f):
    vowel_count = 0
    double_check = False
    bad_slice_check = True
    last = ''

    for c in line:
        if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
            vowel_count += 1

        if c == last:
            double_check = True

        if (last + c) == "ab" or (last + c) == "cd" or (last + c) == "pq" or (last + c) == "xy":
            bad_slice_check = False

        last = c

    if vowel_count >= 3 and double_check and bad_slice_check:
        nice_count += 1

print(nice_count)
f.close()

f = open('day5input.txt')
nice_count = 0

for line in iter(f):
    pair_repeat = False
    prior_repeat = False

    for i in range(0, (len(line) - 2)):
        if line[i] == line[i + 2]:
            prior_repeat = True

        if line[i] + line[i + 1] in line[i + 2:]:
            pair_repeat = True

    if prior_repeat and pair_repeat:
        nice_count += 1

print(nice_count)
f.close()