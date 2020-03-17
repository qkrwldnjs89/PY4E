fn = input('Enter file name: ')
fh = open(fn)
lst = list()

for line in fh :
    words=line.split()
    lst.append(words)

lst = lst[0] + lst[1] + lst[2] + lst[3]
lst.sort()
print(list(set(lst)))
