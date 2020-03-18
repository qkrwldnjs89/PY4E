import re
name = input('Enter file:')
if len(name) < 1 :
    name = 'regex_sum_42.txt'
hand = open(name)

numlists = []
for line in hand :
    line = line.rstrip()
    num = re.findall('[0-9]+',line)
    if len(num) < 1 : continue
    numlists.append(num)

#print(numlists)


a = 0
for numlist in numlists :
    for n in numlist :
        a = a + int(n)
print(a)
