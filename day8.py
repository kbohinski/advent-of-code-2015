f = open('day8input.txt')

lines = f.readlines()
num_chars = 0
num_values = 0
num_code = 0

for i in lines:
    i = i.rstrip()
    num_chars += len(i)
    num_values += len(eval(i))
    num_code += (i.count("\\") + i.count("\"") + 2)

print(num_chars - num_values)
print(num_code)
