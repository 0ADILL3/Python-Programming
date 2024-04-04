class CaesarChiper:
    def __init__(self):
        self.alphabet = "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        # self.alphabet = "azbycxdwevfugthsirjqkplomn AZBYCXDWEVFUGTHSIRJQKPLOMN"
        # self.alphabet = "qwertyuiopasdfghjklzxcvbnm QWERTYUIOPASDFGHJKLZXCVBNM"
        self.modes = {"encrypt" : 1, "decrypt" : -1}
    def crypt(self, text: str, shift: int, mode: str = 'encrypt' or 'decrypt'):
        chiperText = ""
        
        for char in text:
            enc = ((self.alphabet.index(char) + (shift * self.modes[mode])) % len(self.alphabet))
            chiperText = chiperText + self.alphabet[enc]
        
        return chiperText

caesarchiper = CaesarChiper()

plainText = str(input("Plain Text : "))
numbershift = int(input("Shift      : "))
mode = str(input("Mode       : "))

print("Output     :", caesarchiper.crypt(plainText, numbershift, mode))