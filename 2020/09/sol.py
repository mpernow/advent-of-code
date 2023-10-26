f = open('numbers' ,'r')
#f = open('test' ,'r')
numbers = f.readlines()
f.close()

numbers = [int(number.replace('\n','')) for number in numbers]
#print(numbers)

def is_in_list(number, previous):
#    print(number, previous)
    for i in range(len(previous)):
        for j in range(i, len(previous)):
            if previous[i] + previous[j] == number:
                return True
    return False


def find_error(numbers, preamble):
    for i in range(preamble, len(numbers)):
        if not is_in_list(numbers[i], numbers[i-preamble:i]):
            return numbers[i]
    return -1

#invalid = find_error(numbers, 5)
invalid = find_error(numbers, 25)
print(invalid)

def find_weakness(numbers, invalid):
    i = -1
    j = i + 1
    tot = 0
    while tot != invalid:
        i += 1
        j = i + 1
        tot = numbers[i] + numbers[j]
        while tot < invalid:
            j += 1
            tot += numbers[j]
#            print(i,j, tot)
    l = numbers[i:j+1]
    return max(l) + min(l)


print(find_weakness(numbers, invalid))
