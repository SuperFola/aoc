with open("day4.txt") as f:
    content = [
            dict(
                e.split(':') for e in l.replace('\n', ' ').split(' ') if e != ''
            ) for l in f.read().split('\n\n') if l != ''
    ]

fields = [
    'byr', 'iyr', 'eyr',
    'hgt', 'hcl', 'ecl',
    'pid',
]

valid = 0

for data in content:
    print(data)
    if all(k in data.keys() for k in fields):
        valid += 1

print(valid)
