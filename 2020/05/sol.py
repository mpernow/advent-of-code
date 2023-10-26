import math

f = open('seats.dat', 'r')
seats = f.readlines()
seats = [seat.replace('\n','') for seat in seats]



def get_ID(seat):
    lo = 0
    hi = 127
    for i in range(7):
        if seat[i] == 'F':
           lo = lo
           hi = math.floor((hi + lo)/2)
        elif seat[i] == 'B':
             lo = math.ceil((hi + lo)/2)
    left = 0
    right = 7
    for i in range(7,10):
        if seat[i] == 'L':
           right = math.floor((left + right)/2)
        elif seat[i] == 'R':
             left = math.ceil((left + right)/2)
    return lo * 8 + left

IDs = []
for seat in seats:
    IDs.append(get_ID(seat))

print(max(IDs))

IDs.sort()
diff = [IDs[i] - IDs[i+1] for i in range(len(IDs)-1)]
to_left = IDs[diff.index(-2)]
to_right = IDs[diff.index(-2)+1]
print((to_right + to_left)/2)