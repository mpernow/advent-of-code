f = open('timetable','r')
#f = open('test','r')
lines = f.readlines()
f.close()

time = int(lines[0].replace('\n',''))

buses = lines[1].replace(',x','').split(',')
buses = [int(bus) for bus in buses]

#print(time)
#print(buses)


earliest = [bus - (time % bus) for bus in buses]
#print(earliest)
print(buses[earliest.index(min(earliest))]*min(earliest))

#Part 2
buses = lines[1].split(',')
remainders = []
nums = []
for i in range(len(buses)):
    if buses[i] != 'x':
        nums.append(int(buses[i]))
        remainders.append((int(buses[i]) - i) % int(buses[i]))
#print(remainders, nums)

product = 1
for num in nums:
    product *= num
#print(product)

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

B = [product // num for num in nums] # integer division
x = [modinv(B[i], nums[i]) for i in range(len(nums))]
s = [B[i] * remainders[i] * x[i] for i in range(len(B))]
print(sum(s) % product)
