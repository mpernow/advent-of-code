f = open('deck', 'r')
#f = open('test', 'r')
deck = [line.replace('\n','') for line in f.readlines()]
f.close()

i = deck.index('')
p1 = [int(c) for c in deck[1:i]]
p2 = [int(c) for c in deck[i+2:]]

#print(p1,p2)

def play(p1, p2):
    card1 = p1[0]
    card2 = p2[0]
    if card1 > card2:
        p1 = p1[1:]+[card1]+[card2]
        p2 = p2[1:]
    else:
        p2 = p2[1:]+[card2]+[card1]
        p1 = p1[1:]
    return p1,p2

#print(p1,p2)
while (len(p1)>0) and (len(p2)>0):
    p1,p2 = play(p1,p2)
#print(p1,p2)
winner = p1 if len(p1)>0 else p2
#print(winner)
score = sum([i * winner[-i] for i in range(1,len(winner)+1)])
print(score)

# Part 2
p1 = [int(c) for c in deck[1:i]]
p2 = [int(c) for c in deck[i+2:]]

def game(p1,p2):
    played = []
    while (len(p1)>0) and (len(p2)>0):
        if [p1,p2] in played:
            return 'p1',p1,p2
        else:
            played.append([p1,p2])
#            print(played)
            c1 = p1[0]
            c2 = p2[0]
            if (c1 <= len(p1[1:])) and (c2 <= len(p2[1:])):
                winner,_,_ = game(p1[1:c1+1],p2[1:c2+1])
                if winner == 'p1':
                    p1 = p1[1:]+[c1]+[c2]
                    p2 = p2[1:]
                else:
                    p2 = p2[1:]+[c2]+[c1]
                    p1 = p1[1:]
            else:
                if c1>c2:
                    p1 = p1[1:]+[c1]+[c2]
                    p2 = p2[1:]
                else:
                    p2 = p2[1:]+[c2]+[c1]
                    p1 = p1[1:]
    if len(p2)==0:
        return 'p1',p1,p2
    else:
        return 'p2',p1,p2
win,p1,p2 = game(p1,p2)
#print(p1,p2)
if win == 'p1':
    print(sum([i * p1[-i] for i in range(1,len(p1)+1)]))
else:
    print(sum([i * p2[-i] for i in range(1,len(p2)+1)]))
