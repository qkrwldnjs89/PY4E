name = input('Enter file:')
if len(name) < 1 : name = 'mbox-short.txt'
handle = open(name)
awds = []

for line in handle :
    if line.startswith('From ') :
        line = line.rstrip()
        wds = line.split()
        awds.append(wds[5])
# print(awds)

alltime = []
for time in awds :
    alltime.append(time[:2])
# print(alltime)

di = dict()
for hr in alltime :
    di[hr] = di.get(hr,0) + 1
# print(di)

tmp = []
for k,v in di.items() :
    newt = (k,v)
    tmp.append(newt)
# print(tmp)

tmp = sorted(tmp)
for k,v in tmp :
    print (k,v)
