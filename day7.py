f = open('day7input.txt')

lines = f.readlines()
wires = {}


def val_helper(line, i):
    curr_wire = line[i]
    if curr_wire.isdigit():
        val = int(curr_wire)
    elif curr_wire in wires.keys():
        val = wires[curr_wire]
    else:
        val = find_wire_val(curr_wire)
    return val


def find_wire_val(wire):
    if wire in wires.keys():
        return wires[wire]
    else:
        for i in lines:
            i = i.split()
            result_wire = i[-1]
            if wire == result_wire:
                if len(i) == 3:
                    wires[result_wire] = val_helper(i, 0)
                elif i[0] == "NOT":
                    wires[result_wire] = 65535 - val_helper(i, 1)
                elif i[1] == "AND":
                    wires[result_wire] = val_helper(i, 0) & val_helper(i, 2)
                elif i[1] == "OR":
                    wires[result_wire] = val_helper(i, 0) | val_helper(i, 2)
                elif i[1] == "LSHIFT":
                    shift_by = int(i[2])
                    wires[result_wire] = val_helper(i, 0) << shift_by
                elif i[1] == "RSHIFT":
                    shift_by = int(i[2])
                    wires[result_wire] = val_helper(i, 0) >> shift_by
        return wires[wire]


print(find_wire_val("a"))

wires.clear()
wires = {"b": find_wire_val("a")}
print(find_wire_val("a"))
