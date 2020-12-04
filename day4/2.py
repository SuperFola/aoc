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
        byr = len(data['byr']) == 4 and data['byr'].isdigit() and 1920 <= int(data['byr']) <= 2002
        iyr = len(data['iyr']) == 4 and data['iyr'].isdigit() and 2010 <= int(data['iyr']) <= 2020
        eyr = len(data['eyr']) == 4 and data['eyr'].isdigit() and 2020 <= int(data['eyr']) <= 2030
        hgt1 = (data['hgt'][-2:] == 'in' and data['hgt'][:-2].isdigit() and  59 <= int(data['hgt'][:-2]) <= 76)
        hgt2 = (data['hgt'][-2:] == 'cm' and data['hgt'][:-2].isdigit() and 150 <= int(data['hgt'][:-2]) <= 193)
        hcl = len(data['hcl']) == 7 and data['hcl'][0] == '#' and all(e.lower() in "0123456789abcdef" for e in data['hcl'][1:])
        ecl = data['ecl'] in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')
        pid = len(data['pid']) == 9 and data['pid'].isdigit()

        if byr and iyr and eyr and (hgt1 or hgt2) and hcl and ecl and pid:
            valid += 1

print(valid)
