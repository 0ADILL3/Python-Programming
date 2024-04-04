def mapping(var, x1: int, x2: int, y1: int, y2: int, type: str = 'int' or 'float'):
    if(var < x1):
        var = x1
    elif(var > x2):
        var = x2
    else:
        var = (y1 + ((var - x1) * ((y2 - y1) / (x2 - x1))))
    
    if(type == 'int'):
        return int(var)
    elif(type == 'float'):
        return float(var)

# for x in range(77, 126):
#     print(mapping(x, 77, 126, 44, 63, "int"))