with open("day3.txt") as f:
    content = f.readlines()

trees = 0
x = 0
for y, line in enumerate(content):
    if content[y][x % len(content[y])] == "#":
        trees += 1
    x += 3

print(trees)
