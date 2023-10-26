f = open('pw_rules.dat', 'r')
#f = open('test.dat', 'r')
pw_rules = f.readlines()
f.close()

pw_rules = [str(rule) for rule in pw_rules]

rules = []
pws = []
fewest = []
most = []
char = []

for entry in pw_rules:
    rule, pw = entry.split(':')
    char.append(rule[-1].strip(' '))
    f, m = rule[:-2].split('-')
    fewest.append(int(f))
    most.append(int(m))
    pws.append(pw.strip(' ').strip('\n'))

correct = 0
for i in range(len(pws)):
    count = pws[i].count(char[i])
    if (count >= fewest[i]) and (count <= most[i]):
       correct += 1
print(correct)

def check(pw, ind, char):
    if len(pw) < ind:
       return False
    else:
       return pw[ind-1] == char

correct = 0
for i in range(len(pws)):
    if (check(pws[i], fewest[i], char[i])) != (check(pws[i], most[i], char[i])):
       #print(pws[i], fewest[i], most[i], char[i])
       correct += 1
print(correct)

