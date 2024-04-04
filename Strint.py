# def strint(string):
#     result = 0
#     sign = 1
#     for x, y in zip(string, range((len(string) - 1), -1, -1)):
#         if((x == "-") and (y == (len(string) - 1))):
#             sign = -1
#         elif((ord(x) >= 48) and (ord(x) <= 57)):
#             result += ((ord(x) - 48) * (10 ** y))
#         else:
#             result = 0
#             break
#     return result * sign

# num = "-32767"
# print("original ", num)
# print("strint   ", strint(num))
# print("int      ", int(num))
# print("float    ", float(num))
# print("int float", int(float(num)))
# if(float(num) == -32767):
#     print("is number")