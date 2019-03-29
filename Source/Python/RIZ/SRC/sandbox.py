def pack1(tup) :
    return (tup[0]<<8)|tup[1]

def pack(tup) :
#     reversed(tup)
    sum = 0
    for i in range(len(tup)) :
        print(i)
        sum |= tup[i]<<(i<<3)
    return sum

respsum =  (0x12,0x15)
print(hex(pack(respsum[::-1])))
respsum =  (0x12,0x15,0x25,0x35)
print(hex(pack(respsum[::-1])))
respsum = pack(tuple (0x12,0x15,0x25))
print(hex(pack(respsum)))
respsum = tuple(0x12)
print(hex(pack(respsum[::-1])))