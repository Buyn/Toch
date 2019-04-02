def printbit(x):
    for i in range (8):
        print(bin(x >> i&1))
        print(x >> i&1)
     
    
x = 200
print(bin(x))
printbit(x)
# for i in range (8):
#     x >>=1
#     print(bin(x))
# x = 200
# for i in range (8):
#     x <<=2
#     print(bin(x))