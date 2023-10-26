f = open('tickets', 'r')
#f = open('test', 'r')
#f = open('test2', 'r')
tickets = f.readlines()
f.close()


idxs = [i for i, val in enumerate(tickets) if val == '\n']
defs = tickets[:idxs[0]]
my = tickets[idxs[0]+2:idxs[1]]
nearby = tickets[idxs[1]+2:]

#print(defs)
#print(my)
#print(nearby)

tmp = [i.split(': ')[1].replace('\n', '').split(' or ') for i in defs]
tmp = [[r.split('-') for r in t] for t in tmp]
#print(tmp)

valid = []
for t in tmp:
    for r in t:
        valid += range(int(r[0]), int(r[1])+1)
#valid.sort()
#print(valid)

nearby = [ticket.replace('\n','').split(',') for ticket in nearby]
nearby = [[int(entry) for entry in ticket] for ticket in nearby]

err = 0
bad = []
for ticket in nearby:
    for entry in ticket:
        if entry not in valid:
            err += entry
            if ticket not in bad:
                bad.append(ticket)
#            print(entry)
print(err)

# Part 2

for ticket in bad:
    nearby.remove(ticket)
my = [my[0].replace('\n','').split(',')]
my = [int(a) for a in my[0]]
nearby.append(my)
#print(nearby)


valid = [list(range(int(t[0][0]), int(t[0][1])+1)) + list(range(int(t[1][0]), int(t[1][1])+1)) for t in tmp]
#print(valid)

#def invalid_fields(num):
#    tmp = [num in a for a in valid]
#    return [i for i, val in enumerate(tmp) if val == False]

valid_cols = []
for field in valid:
    tmp = list(range(len(valid)))
    for column in range(len(valid)):
        for ticket in nearby:
            if ticket[column] not in field:
                if column in tmp:
                    tmp.remove(column)
    valid_cols.append(tmp)
    print(len(tmp))
print(valid_cols)

for i in range(15):
    for col in valid_cols:
        if len(col) == 1:
            for col2 in valid_cols:
                if (col[0] in col2) and (col != col2):
                    col2.remove(col[0])
    print([len(col) for col in valid_cols])
    print(valid_cols)

print(valid_cols)

tot = 1
print(nearby[-1])
for i in valid_cols[:6]:
    tot *= nearby[-1][i[0]]
print(tot)
