def fRange(start: float, stop: float, step: float):
    eks = 0
    veks = step
    while(eks < 16):
        veks = veks * (10)
        eks = eks + 1
        # print("eksponential :", eks)
        # print("%i == %f == %f" %(veks, veks, int(veks) - veks))
        if((int(veks) - veks) == 0.0) or (((int(veks) - veks) <= 0.00000001) and ((int(veks) - veks) >= -0.00000001)):
            # print("achieved")
            break
        # else:
        #     print("remain")
    
    start = start * (10 ** eks)
    stop = stop * (10 ** eks)
    step = step * (10 ** eks)
    val = start
    data = []
    
    while((val < stop) and (step > 0)) or ((val > stop) and (step < 0)):
        if(eks >= 15):
            break
        data.append(val / (10 ** eks))
        val = float(val + step)
    
    return data

# for x in fRange(1.234, 6.5535, 0.098):
#     print(x)