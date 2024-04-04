def makeList(*element, initial = None, mode: str = 'Multi Dimension Array' or 'Single Array'):
    data = []
    
    if(mode == 'Single Array'):
        for i in element:
            data.append(i)
    
    elif(mode == 'Multi Dimension Array'):
        pointer = 0
        if(len(element) > 0):
            for i0 in range(element[0]):
                pointer = 1
                if((len(element) - pointer) != 0):
                    data.append([])
                else:
                    data.append(initial)

                if(len(element) > 1):
                    for i1 in range(element[1]):
                        pointer = 2
                        if((len(element) - pointer) != 0):
                            data[i0].append([])
                        else:
                            data[i0].append(initial)
                        
                        if(len(element) > 2):
                            for i2 in range(element[2]):
                                pointer = 3
                                if((len(element) - pointer) != 0):
                                    data[i0][i1].append([])
                                else:
                                    data[i0][i1].append(initial)
                                
                                if(len(element) > 3):
                                    for i3 in range(element[3]):
                                        pointer = 4
                                        if((len(element) - pointer) != 0):
                                            data[i0][i1][i2].append([])
                                        else:
                                            data[i0][i1][i2].append(initial)

                                        if(len(element) > 4):
                                            for i4 in range(element[4]):
                                                pointer = 5
                                                if((len(element) - pointer) != 0):
                                                    data[i0][i1][i2][i3].append([])
                                                else:
                                                    data[i0][i1][i2][i3].append(initial)
                                                
                                                if(len(element) > 5):
                                                    for i5 in range(element[5]):
                                                        pointer = 6
                                                        if((len(element) - pointer) != 0):
                                                            data[i0][i1][i2][i3][i4].append([])
                                                        else:
                                                            data[i0][i1][i2][i3][i4].append(initial)

                                                        if(len(element) > 6):
                                                            for i6 in range(element[6]):
                                                                pointer = 7
                                                                if((len(element) - pointer) != 0):
                                                                    data[i0][i1][i2][i3][i4][i5].append([])
                                                                else:
                                                                    data[i0][i1][i2][i3][i4][i5].append(initial)
                                                                
                                                                if(len(element) > 7):
                                                                    for i7 in range(element[7]):
                                                                        pointer = 8
                                                                        if((len(element) - pointer) != 0):
                                                                            data[i0][i1][i2][i3][i4][i5][i6].append([])
                                                                        else:
                                                                            data[i0][i1][i2][i3][i4][i5][i6].append(initial)
    return data

# x = makeList(4, 3, 2, initial=0, mode = "Multi Dimension Array")
# print(x)
# x = makeList(4, 3, 2, mode = "Single Array")
# print(x)

# ===========================================================================================

# x = []
# print(x)
# x = [0, 1, 2, 3]
# print(x)
# x.clear()
# print(x)
# x = 0
# print(x)
# x = 0, 1
# print(x)

# x = [None]
# print(x)
# x[0] = 0
# print(x)
# x.append(None)
# print(x)
# x[0] = None
# print(x)
# x[0] = 1
# x[1] = 1
# print(x)
# x[0] = "ok"
# x[1] = "OK"
# print(x)
# x[0] = None
# print(x)

# x = [[[1], [2]], [[3], [4]]]
# print(x[0][0][0])
# print(x[0][1][0])
# print(x[1][0][0])
# print(x[1][1][0])

# x = [[9, 8, 7], [6, 5, 4]]
# x = [[[]], [[]], [[]]]
# x[0].append(99)
# x[0].append(88)
# x[0][0].append(111)
# x[0][0].append(444)
# x[1].append(77)
# x[1].append(66)
# x[1][0].append(222)
# x[2].append(55)
# x[2].append(44)
# x[2][0].append(333)
# print(x)

# x = [[[]]]
# x.append(1)
# x.append(2)
# x[0].append(1)
# x[0].append(2)
# x[0][0].append(1)
# x[0][0].append(2)
# print(x)

# x = [[[]]]
# x.append(0)
# x[0].append(0)
# x[0][0].append(0)
# x.append([1, 1])
# print(x)

# x = [[[]]]
# for i in range(3):
#     x.append(0)
# print(x)

# x = []
# for i0 in range(4):
#     x.append([])
#     for i1 in range(3):
#         x[i0].append([])
#         for k in range(2):
#             x[i0][i1].append([])
# print(x)

# x[1][1][1] = 99
# print(x)

# for l in x:
#     print(l)
#     for m in l:
#         print(m)
#         for n in m:
#             print(n)


