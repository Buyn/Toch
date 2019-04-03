def printbit(x):
    for i in range (16):
        if x >> i&1 :
            print(i)
def setbit(x, i):
        x << i &1 
        return x
#     
# # x = 0xffff
# x = 32768
# x = 16384
# x = 8192
# print(x)
# print(bin(x))
# printbit(x)
# for i in range (16):
#     print(bin(x << i&1))
