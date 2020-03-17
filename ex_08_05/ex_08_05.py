fn = input('Enter file name: ')
if len(fn) < 1 :
    fn = 'mbox-short.txt'

fh = open(fn)
count = 0
for lx in fh:
    if lx.startswith('From:') :
        continue
    if lx.startswith('From') :
        ly = lx.split()
        print(ly[1])
        count = count + 1

print('There were', count, 'lines in the file with From as the first word')
