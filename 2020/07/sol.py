import copy

f = open('bags.dat', 'r')
#f = open('test.dat', 'r')
#f = open('test2.dat', 'r')
bags = f.readlines()
f.close()

bags = [bag.replace('\n','').split(' contain ') for bag in bags]
# Remove period, plurals
bags = [[bag.replace('bags','bag').replace('.','') for bag in entry] for entry in bags]
bags = [[bag[0]] + [bag[1].split(', ')] for bag in bags]

# Remove numbers:
bags_no_num = bags[:]
for bag in bags:
    tmp = copy.deepcopy(bag)
    for i in range(len(tmp[1])):
        if tmp[1][i][0].isdigit():
           tmp[1][i] = tmp[1][i][2:]
    bags_no_num.append(tmp)
# print(bags)


my_bag = 'shiny gold bag'

candidates = []
for bag in bags_no_num:
    if (my_bag in bag[1]) and (bag[0] not in candidates):
       candidates.append(bag[0])

new = ['']
while len(new) != 0:
      new = []
      for candidate in candidates:
          for bag in bags_no_num:
	          if ((candidate in bag[1]) and (bag[0] not in candidates) and (bag[0] not in new)):
	             new.append(bag[0])
      candidates += new
print(len(candidates))

#print(dict(bags))
bag_dict = dict(bags)
def get_num(bag):
#    print(bag)
    if bag_dict[bag] == ['no other bag']:
#       print('no other')
       return 1
    else:
        result = 1
        for sub_bag in bag_dict[bag]:
#            print(sub_bag)
            result += int(sub_bag[0]) * get_num(sub_bag[2:])
        return result
print(get_num(my_bag)-1)


