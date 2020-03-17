largest = None
smallest = None
while True :
    snum = input('Enter a number: ')
    if snum == 'done' :
        break
    try:
        fnum = int(snum)
    except:
        print('Invalid input')
        continue
    if largest is None :
        largest = fnum
    elif largest < fnum :
        largest = fnum

    if smallest is None :
        smallest = fnum
    elif smallest > fnum :
        smallest = fnum

print('Maximum is', largest)
print('Minimum is', smallest)
