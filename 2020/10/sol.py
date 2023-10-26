f = open('adapters','r')
#f = open('test', 'r')
#f = open('test2', 'r')
adapters = f.readlines()
f.close()

adapters = [int(adapter.replace('\n','')) for adapter in adapters]

adapters.sort()


print(len(adapters))

def next(current, adapters):
    i = 0
    while adapters[i] <= current:
        i += 1
    return adapters[i]


step1 = 0
step3 = 1
current = 0

while current < adapters[-1]:
    tmp = next(current, adapters)
    if tmp - current == 1:
        step1 += 1
    elif tmp - current == 3:
        step3 += 1
    current = tmp

print(step1*step3)


# The sorted list of adapters is one arrangement. All others can be found by removing intermediate ones

def can_remove(ind, adapters):
    if ind == 0:
        return False#(adapters[ind+1] <= 3)
    elif ind == len(adapters) - 1:
        return False
    else:
        return (adapters[ind+1] - adapters[ind-1] <= 3)

# Write a recursive function to remove as a tree structure until we have no more viable ones

adapters = [0] + adapters

def num_combs(adapters, i=0):
    # i is input (recently removed) to avoid overcounting
    if (len(adapters) == 1) or (len(adapters) == 2):
        return 1
    num = 1
    while i < len(adapters):
        if can_remove(i, adapters):
            tmp = adapters.copy()
            tmp.pop(i)
            num += num_combs(tmp, i)
        i += 1
    return num

#print(adapters)
adapters_split = []
i = 0
j = 0
for j in range(len(adapters)):
    if j == len(adapters) - 1:
        adapters_split.append(adapters[i:j+1])
    elif (adapters[j+1] - adapters[j]) >= 3:
        adapters_split.append(adapters[i:j+1])
        i = j+1


prod = 1
for a in adapters_split:
    prod *= num_combs(a)
print(prod)
