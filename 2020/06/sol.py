from itertools import groupby, zip_longest

f = open('answers.dat', 'r')
#f = open('test.dat', 'r')
lines = f.readlines()
f.close()

i = (list(g) for _, g in groupby(lines, key='\n'.__ne__))
answers = [a + b for a, b in zip_longest(i, i, fillvalue=[])]

for i in range(len(answers)):                           
    for j in range(len(answers[i])):                    
        answers[i][j] = answers[i][j].replace('\n','')
    if '' in answers[i]:
       answers[i].remove('')


joint = []
for group in answers:
    tmp = ''
    for answer in group:
        tmp += answer
    joint.append(tmp)


num_unique = []
for answer in joint:
    unique = ''
    for question in answer:
        if not question in unique:
           unique += question
    num_unique.append(len(unique))


print(sum(num_unique))


num_all = []
for i in range(len(answers)):
    n = len(answers[i])
    common = ''
    for question in joint[i]:
        if (joint[i].count(question) == n) and (question not in common):
           common += question
           joint[i].replace(question, '')
    num_all.append(len(common))

print(sum(num_all))