with open("day5.txt") as f:
    content = [l.replace('\n', '') for l in f.readlines()]

seats = list()

columns = {
    "LLL": 0,
    "LLR": 1,
    "LRL": 2,
    "LRR": 3,
    "RLL": 4,
    "RLR": 5,
    "RRL": 6,
    "RRR": 7,
}

for line in content:
    row = line[:7]
    i = [0, 127]
    for c in row:
        if c == "F":
            i[1] = i[0] + (i[1] - i[0]) // 2
        elif c == "B":
            i[0] += (i[1] - i[0]) // 2 + 1
    seats.append(i[0 if c == "F" else 1] * 8 + columns[line[7:]])

print(max(seats))
