fn = input('Enter file name: ')
fh = open(fn)
a=0
b=0
for lx in fh:
    if lx.startswith('X-DSPAM-Confidence:') :
        # print(lx)
        a=a+1
        b=b+float(lx[19:])

# print(a)
# print(b)
c=b/a
print('Average spam confidence:',c)
