import re

f = open('input', 'r')
#f = open('test', 'r')
#f = open('test2', 'r')
lines = [line.replace('\n','').replace('"','') for line in f.readlines()]
f.close()

l = [j for j, val in enumerate(lines) if val == ''][0]
rules = {int(rule.split(':')[0]): rule.split(':')[1][1:] for rule in lines[:l]}
messages = lines[l+1:]
#print(l)

def rec_rule(rule0, rules):
    rule0_lst = rule0.split(' ')
    new_lst = []
    for rule in rule0_lst:
        if rule.isdigit():
            new_lst.append('( '+rules[int(rule)]+' )')
        else:
            new_lst.append(rule)
    return ' '.join(new_lst)

rule0 = rules[0]
while any(char.isdigit() for char in rule0):
#    print(rule0)
    rule0 = rec_rule(rule0, rules)
#print(rule0)


rule0 = '^'+rule0.replace(' ','')+'$'
#print(rule0)
correct = 0
for message in messages:
    if re.match(rule0, message) != None:
        correct += 1
print(correct)


# Part 2
rules[8] = '42 | 42 8'
rules[11] = '42 31 | 42 11 31'


rule0 = rules[0]
#while any(char.isdigit() for char in rule0):
for i in range(100):
#    print(rule0)
    rule0 = rec_rule(rule0, rules)
# End the infinite recursion here!
rule0.replace('8', '(.)+')
rule0.replace('11', '(.)+')
#print(rule0)


rule0 = '^'+rule0.replace(' ','')+'$'
#print(rule0)
correct = 0
for message in messages:
    if re.match(rule0, message) != None:
        correct += 1
print(correct)
