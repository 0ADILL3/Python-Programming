from PBB import FindPBB
pbb = FindPBB()

class RSA:
    def __init__(self):
        self.p = 0
        self.q = 0
        self.keyPair = []
        
        self.m = 0
        self.n = 0
    
    def generateKey(self, p: int, q: int, e_range: int, d_range: int):
        n = p * q
        m = (p - 1) * (q - 1)
        self.n = n
        self.m = m
        
        k = 0
        
        for e in range(e_range):
            if(pbb.PBB(e, m) == 1):
                self.keyPair.append([e])
        
        for e in range(len(self.keyPair)):
            d = 0
            k = 0
            while(d < d_range):
                d = (1 + (k * m)) / self.keyPair[e][0]
                if(d == int(d)):
                    self.keyPair[e].append(int(d))
                # print(e, self.keyPair[e][0], d)
                k = k + 1
        return self.keyPair
    
    def crypt(self, plainText: str, e: int, d: int, *, mode = 'encrypt' or 'decrypt'):
        chiperText = []
        asciiText = []
        for char in plainText:
            asciiText.append(char)
        
        for chiper in asciiText:
            if(mode == 'encrypt'):
                chiperText.append((chiper ** e) % self.n)
                # chiperText.append(chr((chiper ** e) % self.n))
            if(mode == 'decrypt'):
                chiperText.append((chiper ** d) % self.n)
                # chiperText.append(chr((chiper ** d) % self.n))
        return chiperText

rsa = RSA()
print(rsa.generateKey(23, 31, 100, 1000))

pText = [72, 101, 108, 108, 111, 44, 32, 87, 111, 114, 108, 100, 33]
# cText = [485, 188, 271, 271, 567, 332, 280, 397, 567, 321, 271, 679, 221] # e = 7, d = 283
# cText = [9, 357, 647, 647, 237, 42, 311, 25, 237, 22, 647, 639, 659] # e = 13, d = 457
# cText = [71, 326, 616, 616, 268, 631, 280, 397, 268, 22, 616, 81, 566] # e = 73, d = 217
cText = [547, 2, 54, 54, 102, 270, 94, 242, 102, 321, 54, 400, 66] # e = 97, d = 313
# for i in pText:
#     text.append(ord(i))
# print(pText)

print(pText)
print(rsa.crypt(pText, 97, 313, mode = 'encrypt'))
print(rsa.crypt(cText, 97, 313, mode = 'decrypt'))

# =======================================================================================

# print(((2 ** 339) - 1))
# print(((2 ** 339) - 1) / 11)


# text = "HELLO WORLD"
# # text = [726, 976, 767, 932, 877, 982, 766, 8]
# # text = [446, 60, 58, 16, 255, 685, 396, 35]
# chiper = ""
# chiper2 = ""
# try:
#     # print(726 ** 29)
    
#     # print((72 ** 29) % 713)
#     # print((277 ** 569) % 713)
    
#     # print((726 ** 79) % 3337)
#     # print((215 ** 1019) % 3337)
    
#     for c in text:
#         # chiper.append(((ord(c) ** 29) % 713))
        
#         chiper = chiper + chr(((ord(c) ** 29) % 713))
#         chiper2 = chiper2 + str(((ord(c) ** 29) % 713)) + " "
#         # chiper = chiper + chr(((c ** 29) % 713))
#         # chiper2 = chiper2 + str(((c ** 569) % 713))
        
#         # chiper2 = chiper2 + str(((c ** 1229) % 713)) + " "
#     print(chiper)
#     print(chiper2)
# except (ValueError, ArithmeticError, BufferError, MemoryError, OverflowError) as e:
#     print(e)


# d = 0
# k = 0
# while(True):
#     d = (1 + (k * 660)) / 29
#     print(k, d)
#     k = k + 1
#     if(d == int(d)) and (d > 570):
#         break


# text = "HELLO WORLD"
# asciiText = ""
# for i in text:
#     asciiText = asciiText + str(ord(i))
# print(asciiText)