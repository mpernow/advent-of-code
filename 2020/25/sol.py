card = 19774466
door = 7290641

#card = 5764801
#door = 17807724

div = 20201227

def one_iteration(num, subj, div = 20201227):
    num *= subj
    num = num % div
    return num

l_card = 0
subj = 7
num = 1
while num != card:
    num = one_iteration(num, subj)
    l_card += 1
print(num, l_card)

l_door = 0
num = 1
while num != door:
    num = one_iteration(num, subj)
    l_door += 1
print(num, l_door)

# Transform card with l_door
i = 0
num = 1
subj = card
while i < l_door:
    num = one_iteration(num, subj)
    i += 1
print(num)

i = 0
num = 1
subj = door
while i < l_card:
    num = one_iteration(num, subj)
    i += 1
print(num)
