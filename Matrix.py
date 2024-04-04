from List import makeList

class Matrix:
    def __init__(self):
        self.matrix = {}
    
    def createMatrix(self, Name: str, Row: int, Column: int):
        self.matrix.update({Name : makeList(Row, Column)})
        return makeList(Row, Column)
    
    def fillMatrix(self):
        for i in self.matrix:
            print('Fill Matrix %s' %i)
            for rr in range(len(self.matrix[i])):
                for rc in range(len(self.matrix[i][0])):
                    self.matrix[i][rr][rc] = int(input('Row %i, Column %i : ' %(rr, rc)))
    
    def crossMatrix(self, A: list, B: list):
        C = makeList(len(A), len(B[0]))
        # m*r and r*n == True
        if(len(A[0]) == len(B)):
            for rr in range(len(C)):
                for rc in range(len(C[0])):
                    summ = 0
                    for ctr in range(len(B)):
                        summ = summ + (A[rr][ctr] * B[ctr][rc])
                    C[rr][rc] = summ
            return C
        else:
            return 'cross product is not defined'
    
    def adderMatrix(self, A: list, B: list):
        C = makeList(len(A), len(A[0]), initial=0)
        if((len(A) == len(B)) and (len(A[0]) == len(B[0]))):
            for rr in range(len(A)):
                for rc in range(len(A[0])):
                    C[rr][rc] = C[rr][rc] + (A[rr][rc] + B[rr][rc])
            return C
        else:
            return 'adder product is not defined'
    
    def subtractMatrix(self, A: list, B: list):
        C = makeList(len(A), len(A[0]), initial=0)
        if((len(A) == len(B)) and (len(A[0]) == len(B[0]))):
            for rr in range(len(A)):
                for rc in range(len(A[0])):
                    C[rr][rc] = C[rr][rc] + (A[rr][rc] - B[rr][rc])
            return C
        else:
            return 'subtract product is not defined'
    
    def transposeMatrix(self, M: list):
        N = makeList(len(M[0]), len(M))
        for rr in range(len(M)):
            for rc in range(len(M[0])):
                N[rc][rr] = M[rr][rc]
        return N
    
    def scalarMatrix(self, M: list, scalar: int = 1):
        N = makeList(len(M), len(M[0]))
        for rr in range(len(M)):
            for rc in range(len(M[0])):
                N[rr][rc] = scalar * M[rr][rc]
        return N
    
    def determineMatrix(self, M: list):
        determine = 0
        if(len(M) == len(M[0])) and (len(M) > 2):
            for pSession in range(len(M[0])):
                summ = 1
                for rr, rc in zip(range(0, len(M[0]), 1), range(0, len(M[0]), 1)):
                    summ = summ * M[rr][(rc + pSession) % len(M[0])]
                determine = determine + summ
            for nSession in range(len(M[0])):
                summ = 1
                for rr, rc in zip(range(len(M[0]) - 1, -1, -1), range(0, len(M[0]), 1)):
                    summ = summ * M[rr][(rc + nSession) % len(M[0])]
                determine = determine - summ
            return determine
        elif(len(M) == len(M[0])) and (len(M) == 2):
            for pSession in range(1):
                summ = 1
                for rr, rc in zip(range(0, len(M[0]), 1), range(0, len(M[0]), 1)):
                    summ = summ * M[rr][(rc + pSession) % len(M[0])]
                determine = determine + summ
            for nSession in range(1):
                summ = 1
                for rr, rc in zip(range(len(M[0]) - 1, -1, -1), range(0, len(M[0]), 1)):
                    summ = summ * M[rr][(rc + nSession) % len(M[0])]
                determine = determine - summ
            return determine
        else:
            return 'determine is not defined'


m = Matrix()
m.createMatrix('matrix a', 3, 3)
m.createMatrix('matrix b', 3, 3)
m.fillMatrix()
print(m.matrix)
for i in m.matrix:
    print(i)
    for r in m.matrix[i]:
        print(r)

for j in m.crossMatrix(m.matrix['matrix a'], m.matrix['matrix b']):
    print(j)
# for j in m.adderMatrix(m.matrix['matrix a'], m.matrix['matrix b']):
#     print(j)
# for j in m.subtractMatrix(m.matrix['matrix a'], m.matrix['matrix b']):
#     print(j)
# for j in m.transposeMatrix(m.matrix['matrix a']):
#     print(j)
# for j in m.scalarMatrix(m.matrix['matrix a'], 2):
#     print(j)
# print(m.determineMatrix(m.matrix['matrix a']))