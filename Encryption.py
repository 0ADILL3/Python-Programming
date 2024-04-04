def crypt(string : str, stringKey : str, initialShiftPosition : int = 1, numberShift : int = 1, mode : int = "encrypt" or "decrypt", shiftInterval : int = 1, lowerLimit : int = 31, upperLimit : int = 126):
    numberMode = {"encrypt" : 1, "decrypt" : -1}
    
    initialShiftPosition = initialShiftPosition * numberMode[mode]
    numberShift = numberShift * numberMode[mode]
    
    textRange = upperLimit - lowerLimit
    shiftPosition = initialShiftPosition
    text = ""
    k = 0
    
    for c in range(0, len(string)):
        if(c % shiftInterval == 0):
            shiftPosition = shiftPosition + numberShift + (ord(stringKey[k]) * numberMode[mode])
            result = ord(string[c]) + shiftPosition
            
            while(result > upperLimit):
                # print("%3i %c >> %3i >> %3i %c <<" %(ord(string[c]), string[c], shiftPosition, result, result))
                result = result - textRange
                # shiftPosition = int(shiftPosition / 5)
                
            while(result < lowerLimit):
                # print("%3i %c >> %3i >> %3i %c <<" %(ord(string[c]), string[c], shiftPosition, result, result))
                result = result + textRange
                # shiftPosition = int(shiftPosition / 5)
                
            # print("%3i %c >> %3i >> %3i %c" %(ord(string[c]), string[c], shiftPosition, result, result))
            text = text + chr(result)
            
        else:
            # print("%3i %c >> %3i >> %3i %c >>" %(ord(string[c]), string[c], 0, ord(string[c]), string[c]))
            text = text + string[c]
        
        k = k + 1
        if(k > (len(stringKey) - 1)):
            k = 0
        if((shiftPosition > 65535) or (shiftPosition < -65535)):
            shiftPosition = 0
    
    return text

# plainText = str(input("Plain Text  : "))
# key1 = str(input("String Key  : "))
# key2 = int(input("Initial     : "))
# key3 = int(input("Number      : "))
# key4 = str(input("Mode        : "))
# key5 = int(input("Interval    : "))
# key6 = int(input("Lower Limit : "))
# key7 = int(input("Upper Limit : "))

# print("Output", crypt(plainText, key1, key2, key3, key4, key5, key6, key7))
# print("Output", crypt(plainText, key1, 1, 1, "encrypt"))