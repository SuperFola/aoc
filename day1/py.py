with open("day1.txt") as f:
    content = list(map(int, f.readlines()))

for i, e in enumerate(content):
    for j, f in enumerate(content[i:]):
        for k, g in enumerate(content[j:]):
            if e + f + g == 2020:
                print(e * f * g)
