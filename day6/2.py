with open("day6.txt") as f:
    content = [[''.join(sorted(list(k))) for k in e.split('\n') if k != ''] for e in f.read().split('\n\n')]

groups = [0 for _ in range(len(content))]
for i, data in enumerate(content):
    ans = {}
    print(data)
    for people in data:
        for c in people:
            ans[c] = ans.get(c, 0) + 1
    t = 0
    for e in ans.values():
        if e == len(data):
            t += 1
    groups[i] = t

print(sum(groups))
