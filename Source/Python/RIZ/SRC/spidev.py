
class SpiDev(object):
    
    
    def __init__(self):
        pass

    
    def open(self, BUS, DEVICE):
        print("open", BUS, DEVICE)

    
    def xfer2(self, build_read_command):
        print('xfer2', build_read_command)

    
    def writebytes(self, hex):
        print('writebytes', hex)

    
    def close(self):
        print('close')

    
    def xfer(self, param1):
        print('xfer = ', param1)
        return 0

    
    def readbytes(self, param1):
        result = []
        for i in range(param1):
            print(i, " = ", result)
            result.append(i)
        return result
    
    
    
    
    
    
    
    
    
    
    
    

