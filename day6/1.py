with open("day6.txt") as f:
    content = [e.replace('\n', '') for e in f.read().split('\n\n')]

groups = [0 for _ in range(len(content))]
line = ""
for i, data in enumerate(content):
    for c in data:
        if c not in line:
            line += c
    groups[i] = len(line)
    line = ""

print(sum(groups))
