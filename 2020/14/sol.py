from itertools import product

f = open('program', 'r')
#f = open('test', 'r')
#f = open('test2', 'r')
program = f.readlines()
f.close()

program = [line.replace('\n','') for line in program]

idxs = [i for i, line in enumerate(program) if line[:4] == 'mask'] + [len(program)]
program = [program[i:j] for i, j in zip(idxs, idxs[1:])]

#print(program)


mem = {}

def write(mask, instr, mem):
    instr = instr.split(' = ')
    addr = int(instr[0][4:-1])
    val_bin = format(int(instr[1]), 'b').zfill(36)
    for i in range(len(mask)):
        if mask[i] != 'X':
            val_bin = val_bin[:i] + mask[i] + val_bin[i+1:]
    mem[addr] = int(val_bin, 2)


for block in program:
    mask = block[0][7:]
    for instr in block[1:]:
#        print(instr)
        write(mask, instr, mem)

#print(mem)

print(sum(list(mem.values())))


# Paet 2

mem = {}

def get_addr(mask, addr):
    addrs = []
    addr = format(addr, 'b').zfill(36)
    for i in range(len(mask)):
        if mask[i] == '1':
            addr = addr[:i] + '1' + addr[i+1:]
        elif mask[i] == 'X':
            addr = addr[:i] + 'X' + addr[i+1:]
    numx = addr.count('X')
    p = product([0,1], repeat=numx)
    indx = [pos for pos, char in enumerate(addr) if char == 'X']
    for comb in p:
        tmp = addr[:indx[0]]
        for i in range(len(comb) - 1):
            tmp += str(comb[i]) + addr[indx[i]+1:indx[i+1]]
        tmp += str(comb[-1]) + addr[indx[-1]+1:]
        addrs.append(int(tmp, 2))
    return addrs


for block in program:
    mask = block[0][7:]
    for instr in block[1:]:
        instr = instr.split(' = ')
        addr = int(instr[0][4:-1])
        val = int(instr[1])
        addrs = get_addr(mask, addr)
        for addr in addrs:
            mem[addr] = val

print(sum(list(mem.values())))
