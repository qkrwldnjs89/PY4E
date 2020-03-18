import re
name = input('Enter file: ')
if len(name) < 1 : name = 'regex_sum_381353.txt'
hand = open(name)

numlists = []
for line in hand :
    line = line.rstrip()
    num = re.findall('[0-9]+',line)
    if len(num) < 1 : continue
    numlists.append(num)

# print(numlists)

sum = 0
for numlist in numlists :
    for n in numlist :
        sum = sum + int(n)
print(sum)
