start = [16,11,15,0,1,7]
#start = [1,3,2]
#start = [3,1,2]
#start = [0,3,6]

spoken = start[:]

def next(spoken):
    val = spoken[-1]
    if spoken.count(val) == 1:
        return 0
    else:
        idxs = [i for i,v in enumerate(spoken) if v == val]
    return idxs[-1] - idxs[-2]

for i in range(2020):
    spoken.append(next(spoken))
print(spoken[2019])


# Part 2
spoken = start[:]

spoken_dict = {}
for i in range(len(spoken)):
    spoken_dict[spoken[i]] = [i]

latest = spoken[-1]
count = len(spoken)

def next2(latest, count, spoken_dict):
    if len(spoken_dict[latest]) == 1:
        if 0 not in spoken_dict:
            spoken_dict[0] = [count]
        else:
            spoken_dict[0] = [spoken_dict[0][-1], count] 
        return 0
    else:
        diff = spoken_dict[latest][1] - spoken_dict[latest][0]
        if diff not in spoken_dict:
            spoken_dict[diff] = [count]
        else:
            spoken_dict[diff] = [spoken_dict[diff][-1], count]
        return diff

for i in range(30000000-len(spoken)):
    latest = next2(latest, count, spoken_dict)
    count += 1
print(latest)
