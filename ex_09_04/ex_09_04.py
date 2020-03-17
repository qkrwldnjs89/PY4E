name = input('Enter file:')
if len(name) < 1 : name = 'mbox-short.txt'
handle = open(name)
dic = dict()
awds = []

for line in handle:
    if line.startswith('From '):
        line = line.rstrip()
        wds = line.split()
        awds.append(wds[1])
for w in awds :
    dic[w] = dic.get(w,0) + 1
# print(dic)

largest = -1
theword = None

for k,v in dic.items():
    if v > largest:
        largest = v
        theword = k
print(theword,largest)
