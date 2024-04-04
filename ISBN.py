def isbn(booksNumber: str):
    result = 0
    charIndex = 0
    
    index = 1
    for num in booksNumber:
        if((ord(num) >= 48) and (ord(num) <= 57)):
            # print(num, index)
            result = result + (int(num) * index)
            index = index + 1
        elif((ord(num) >= 97) and (ord(num) <= 123)):
            # print(index, num, sep='')
            charIndex = index
            index = index + 1
        if(index > 9):
            break
    
    k = 0
    charValue = 0
    while(True):
        charValue = (11 * k - result) / charIndex
        if((charValue >= 0) and (charValue <= 9) and (charValue == int(charValue))):
            break
        k = k + 1
    # print('%i = (11(%i) - %i) / %i' %(charValue, k, result, charIndex))
    return int(charValue)

print(isbn('0-201-57p859-1'))
print(isbn('1-312-68p960-2'))