cups = [3,8,9,5,4,7,6,1,2]
#cups = [3,8,9,1,2,5,4,6,7]

class CrabCups:
    def __init__(self, cups):
        self.current = cups[0]
        self.next_cup = {}
        for i, c in enumerate(cups, 1):
            self.next_cup[c] = cups[i%len(cups)]
            
    def __iter__(self):
        return self

    def __next__(self):
        remove = []
        to_move = self.current
        for i in range(3):
            remove.append(self.next_cup[to_move])
            to_move = self.next_cup[to_move]
        self.next_cup[self.current] = self.next_cup[remove[2]]
        destination = self.current - 1
        while destination <= 0 or destination in remove:
            if destination == 0:
                destination = len(self.next_cup)
            if destination in remove:
                destination -= 1
        self.next_cup[destination], self.next_cup[remove[2]] = (remove[0], self.next_cup[destination],)
        self.current = self.next_cup[self.current]

    @property
    def final(self):
        current = 1
        output = []
        for _ in range(len(self.next_cup) - 1):
            output.append(self.next_cup[current])
            current = self.next_cup[current]
        output = [str(n) for n in output]
        return ''.join(output)

# Part 1
cc = CrabCups(cups)
for _ in range(100):
    next(cc)
print(cc.final)

# Part 2
cups.extend(range(10, 1000001))
cc = CrabCups(cups)
for _ in range(10000000):
    next(cc)
a = cc.next_cup[1]
b = cc.next_cup[a]
print(a*b)
