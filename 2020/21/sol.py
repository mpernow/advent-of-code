f = open('ingredients', 'r')
#f = open('test', 'r')
ingredients = [line.replace('\n','') for line in f.readlines()]
f.close()

allergens = [ingredient.split('(')[1][9:-1].split(', ') for ingredient in ingredients]
ingredients = [ingredient.split('(')[0][:-1].split(' ') for ingredient in ingredients]

#print(ingredients)
#print(allergens)

recipes = []
possible_alls = {}
recipes_with = {}

for i in range(len(allergens)):
    ings = set(ingredients[i])
    alls = set(allergens[i])
    recipes.append(ings)

    for al in alls:
        if not al in recipes_with:
            recipes_with[al] = [i]
        else:
            recipes_with[al].append(i)
    for ing in ings:
        if not ing in possible_alls:
            possible_alls[ing] = set(alls)
        else:
            possible_alls[ing] |= alls

#print(recipes)
#print(possible_alls)
#print(recipes_with)

safe = []
for ingr, possible in possible_alls.items():
    #print(ingr, possible)
    impossible = set()
    for aller in possible:
        if any(ingr not in recipes[i] for i in recipes_with[aller]):
            impossible.add(aller)
    possible -= impossible
    if not possible:
        safe.append(ingr)
#print(safe)
tot = sum(ingr in r for r in recipes for ingr in safe)
print(tot)

dangerous = {}
for ing in possible_alls:
    if len(possible_alls[ing]) != 0:
        dangerous[ing] = list(possible_alls[ing])
print(dangerous)
while any(len(dangerous[ing]) > 1 for ing in dangerous):
    for ing in dangerous:
        if len(dangerous[ing]) == 1:
            for ing2 in dangerous:
                if (ing2 != ing) and (dangerous[ing][0] in dangerous[ing2]):
                    dangerous[ing2].remove(dangerous[ing][0])
print(dangerous)

d2 = {dangerous[ing][0]:ing for ing in dangerous}
print(d2)

lst = ','.join(map(d2.get, sorted(d2)))
print(lst)
