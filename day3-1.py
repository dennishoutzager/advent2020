def eviski (letsgo):
    tree = 0
    for i, line in enumerate(letsgo):
        if line[(i * 3) % len(line)] == '#':
            tree += 1
    return tree

with open('day3input.txt') as file:
    data = file.read()
letsgo = data.splitlines()
print(eviski(letsgo))
