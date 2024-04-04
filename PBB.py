from Modulus import modulus as md

class FindPBB:
    def __init__(self):
        self.fpbA = []
        self.fpbB = []
        self.fpb = []
    
    def PBB(self, a: int, b: int):
        self.fpbA =  []
        self.fpbB = []
        self.fpb = []
        
        if(a > 0):
            for n in range(1, a + 1, 1):
                if((a % n) == 0):
                    self.fpbA.append(n)
        elif(a < 0):
            for n in range(-1, a - 1, -1):
                if((a % n) == 0):
                    self.fpbA.append(n)
        
        if(b > 0):
            for n in range(1, b + 1, 1):
                if((b % n) == 0):
                    self.fpbB.append(n)
        
        elif(b < 0):
            for n in range(-1, b - 1, -1):
                if((b % n) == 0):
                    self.fpbB.append(n)
        
        for num in self.fpbA:
            if(num in self.fpbB):
                self.fpb.append(num)
        
        # print("FPB a ", self.fpbA)
        # print("FBB b ", self.fpbB)
        # print("FBB ab", self.fpb)
        if(len(self.fpb) > 0):
            # print("PBB  :", max(self.fpb))
            return max(self.fpb)
        else:
            # print("PBB  :", "None")
            return None
    
    def EuclideanPBB(self, a: int, b: int):
        if((a > b) and (b > 0)):
            m = a
            n = b
        elif((a > b) and (b < 0)):
            m = b
            n = a
        elif((b > a) and (a > 0)):
            m = b
            n = a
        elif((b > a) and (a < 0)):
            m = a
            n = b
        
        while(True):
            q = int(m / n)
            r = md.mod(self, m, n)
            # r = m % n
            print("%i = %i(%i) + %i" %(m, n, q, r))
            m = n
            n = r
            if(r == 0):
                break

pbb = FindPBB()

print(pbb.PBB(63, 81))
print(pbb.fpb)
# pbb.EuclideanPBB(34, 5)
# pbb.EuclideanPBB(14, 39)
# pbb.EuclideanPBB(14, -39)
# pbb.EuclideanPBB(-14, 39)
# pbb.EuclideanPBB(-14, -39)