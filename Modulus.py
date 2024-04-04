class modulus:
    def __init__(self):
        self.m = 0
        self.n = 0
        self.q = 0
        self.r = 0
    
    def mod(self, m: int, n: int):
        # m = nq + r
        if((m >= 0) and (n > 0)):
            q = int(m / n)
        elif((m >= 0) and (n < 0)):
            q = int(m / n) - 1
        elif((m < 0) and (n > 0)):
            q = int(m / n) - 1
        elif((m < 0) and (n < 0)):
            q = int(m / n)
        
        r = m - (n * q)
        
        self.m = m
        self.n = n
        self.q = q
        self.r = r
        return r

# m = modulus()
# a = 39
# b = 14

# print(m.mod(a, b), a % b)
# print("%i = %i(%i) + %i" %(m.m, m.n, m.q, m.r))
# print(m.mod(-a, b), -a % b)
# print("%i = %i(%i) + %i" %(m.m, m.n, m.q, m.r))
# print(m.mod(a, -b), a % -b)
# print("%i = %i(%i) + %i" %(m.m, m.n, m.q, m.r))
# print(m.mod(-a, -b), -a % -b)
# print("%i = %i(%i) + %i" %(m.m, m.n, m.q, m.r))

# print(m.mod(a, -b), a % -b)
# print("%i = %i(%i) + %i" %(m.m, m.n, m.q, m.r))
# print("m = %i, n = %i, q = %i, r = %i" %(m.m, m.n, m.q, m.r))

# for i in range(a):
#     print(i, m.mod(i, 10))
# print("%i = %i(%i) + %i" %(m.m, m.n, m.q, m.r))
# print("m = %i, n = %i, q = %i, r = %i" %(m.m, m.n, m.q, m.r))