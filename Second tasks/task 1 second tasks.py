numberlist = []


for x in range(1500, 2701):
    
    if (x % 7 == 0) and (x % 5 == 0):
        
        numberlist.append(str(x))


print(','.join(numberlist))
