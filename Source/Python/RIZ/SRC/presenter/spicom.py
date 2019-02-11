import spidev
from model.globalsvar import * 


class SPICom(object):
    
    
    def __init__(self, address):
        self.address = address
        self.spi = spidev.SpiDev()
        self.spi.max_speed_hz = 18000000
        self.spi.mode = 0b00
        self.spi.lsbfirst = False


    def send(self, word):
        self.spi.open(BUS,DEVICE)
        resp = self.spi.xfer(word)
        self.spi.close()
        print("sent = [ ", word, " ] , resiv = [ ", resp, " ]")
        return resp
    
    
    def sendEOF(self):
        return self.send([SC_ENDOFFILE])
    
    
    def sendExecude(self):
        return self.send([SC_EXECUTECOMMAND])
    
    
    def sendEndSession(self):
        return self.send([SC_ENDOFSESION])
    
    
    def sendWordsList(self, command):
        # send waiting one word
        self.send(hex(len(command)))
        print("lens is = ", hex(len(command)))
        for t in command:
            # send command
            self.send(t)
    
    
    def execute(self, command):
        self.send(self.address)
        self.sendWordsList(command)
        self.sendEOF()
        self.sendExecude()
        self.sendEndSession()
    
    
    # put in Stek
    
    
    
    



