from itertools import groupby, zip_longest
import re

f = open('batch.dat', 'r')
#f = open('test.dat', 'r')
lines = f.readlines()
f.close()

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']

i = (list(g) for _, g in groupby(lines, key='\n'.__ne__))
entries = [a + b for a, b in zip_longest(i, i, fillvalue=[])]

entries = [[l.split(' ') for l in entry] for entry in entries]

passports = []
for entry in entries[:-1]:
    tmp = []
    for l in entry[:-1]:
        tmp+=l
    passports.append(tmp)
tmp = []
for l in entries[-1]:
    tmp += l
passports.append(tmp)

for i in range(len(passports)):
    for j in range(len(passports[i])):
        passports[i][j] = passports[i][j].replace('\n','')
    passports[i].sort()
    for k in range(len(passports[i])-1):
        if passports[i][k][:3] == 'cid':
           passports[i].remove(passports[i][k])


#print(passports)

## Get the ones with all the required fields
fields_present = [[f[:3] for f in entry] for entry in passports]

fields.remove('cid')
fields.sort()

#print(fields)

valids = []

for i in range(len(fields_present)):
    tmp = fields_present[i].copy()
    if 'cid' in tmp:
       tmp.remove('cid')
    tmp.sort()
    if tmp == fields:
       valids.append(i)
print(len(valids))

# Since we have sorted them and removed cid, they all contain the same keys in the same order. So we can access them by index


## Valid birth year (four digits 1920-2002 inclusive)
def check_byr(byr):
    if len(byr) != 4:
       return False
    byr = int(byr)
    if byr < 1920:
       return False
    if byr > 2002:
       return False
    else:
        return True

valids = [valid for valid in valids if check_byr(passports[valid][0][4:])]

#print('byr', valids)





## Valid expiration year (four digits 2020-2030 inclusive)
def check_eyr(byr):
    if len(byr) != 4:
       return False
    byr = int(byr)
    if byr < 2020:
       return False
    if byr > 2030:
       return False
    else:
        return True


valids = [valid for valid in valids if check_eyr(passports[valid][2][4:])]


#print('eyr',valids)


## Valid height (number followed by cm or in, 150-193 cm inclusive or 59-76 in inclusive)
def check_hgt(hgt):
    if hgt[-2:] == 'in':
        if (int(hgt[:-2]) >= 59) or (int(hgt[:-2]) <= 76):
            return True
    elif hgt[-2:] == 'cm':
        if (int(hgt[:-2]) >= 150) or (int(hgt[:-2]) <= 193):
            return True


valids = [valid for valid in valids if check_hgt(passports[valid][4][4:])]


#print('hgt', valids)



## Valid haircolour (a # followed by six characters 0-9 or a-f)
def check_hcl(hcl):
    if not hcl[0] == '#':
       return False
    if not len(hcl) == 7:
       return False
    return bool(re.match('^[a-z0-9]+$', hcl[1:]))


valids = [valid for valid in valids if check_hcl(passports[valid][3][4:])]


#print('hcl', valids)



## Eye colour (one of amb blu brn gry grn hzl oth)
def check_ecl(ecl):
    if ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
       return True
    else:
        return False


valids = [valid for valid in valids if check_ecl(passports[valid][1][4:])]

#print('ecl', valids)




## Passport ID (nine digit number, including leading zeroes)
def check_pid(pid):
    if len(pid) == 9:
       return True
    else:
        return False


valids = [valid for valid in valids if check_pid(passports[valid][6][4:])]


## Valid issue year (four digist 2010-2020 inclusive)
def check_iyr(byr):
    if len(byr) != 4:
       return False
    byr = int(byr)
    if byr < 2010:
       return False
    if byr > 2020:
       return False
    else:
        return True

valids = [valid for valid in valids if check_iyr(passports[valid][5][4:])]

#print('iyr', valids)





print(len(valids))

for valid in valids:
    print(passports[valid][6])