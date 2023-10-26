f = open('code', 'r')
#f = open('test', 'r')
lines = f.readlines()
f.close()

code = [line.replace('\n','') for line in lines]
#print(code)

def run(code):
    acc = 0
    visited = []
    i = 0
    
    while (i not in visited) and (i < len(code)):
          visited.append(i)
          instruction = code[i]
          if code[i][:3] == 'nop':
             i += 1
          elif code[i][:3] == 'acc':
               acc += int(code[i][4:])
               i += 1
          elif code[i][:3] == 'jmp':
               i += int(code[i][4:])
          else:
            RaiseValueError('Instruction not recognised')

    if i == len(code):
       success = True
    else:
        success = False
    return (acc, success)

print(run(code))


jmp_instr = [i for i, j in enumerate(code) if j[:3] == 'jmp']
nop_instr = [i for i, j in enumerate(code) if j[:3] == 'nop']

for i in jmp_instr:
    modified = code[:]
    modified[i] = 'nop '+code[i][4:]
    result = run(modified)
    if result[1] == True:
       print(result)

for i in nop_instr:
    modified = code[:]
    modified[i] = 'jmp '+code[i][4:]
    result = run(modified)
    if result[1] == True:
       print(result)

