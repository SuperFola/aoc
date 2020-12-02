with open("day2.txt") as f:
    content = [e.split(': ') for e in f.readlines()]

for i, e in enumerate(content):
    content[i][1] = content[i][1].replace('\n', '')
    range_, letter = content[i][0].split(' ')
    content[i].insert(1, letter)
    a, b = list(map(int, range_.split('-')))
    content[i][0] = a
    content[i].insert(1, b)

valid = 0
for data in content:
    a, b, letter, passwd = data
    if a <= passwd.count(letter) <= b:
        valid += 1

print(valid)
