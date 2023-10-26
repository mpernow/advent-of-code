import re

f = open('homework' ,'r')
#f = open('test', 'r')
homework = [line.replace('\n','').replace(' ','') for line in f.readlines()]
f.close()

#print(homework)

class Number(int):
    def __add__(self,other):
        return Number(int(self) + int(other))
    def __sub__(self, other):
        return Number(self * other)

sols = [eval(re.sub(r"\d+", lambda match: f"Number({match.group(0)})", task.replace('*', '-'))) for task in homework]
#print(sols)
print(sum(sols))

class Number2(int):
    def __add__(self,other):
        return Number2(int(self) * int(other))
    def __mul__(self,other):
        return Number2(int(self) + int(other))

#print(homework)
sols = [eval(re.sub(r"\d+", lambda match: f"Number2({match.group(0)})",      
                    task.replace('*', '-').replace('+','*').replace('-','+'))) for task in homework]

print(sum(sols))
