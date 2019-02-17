import spidev
from model.globalsvar import * 


class SPICom(object):
    
    
    def __init__(self, address):
        self.address = address
        self.spi = spidev.SpiDev()


    def send(self, word):
        print("sending = [ ", word, " ] ")
        self.spi.open(BUS,DEVICE)
        self.spi.max_speed_hz = 18000000
        self.spi.mode = 0b00
        self.spi.lsbfirst = False
        resp = self.spi.xfer([word])
        self.spi.close()
        print("send = [ ", word, " ] , resiv = [ ", resp, " ]")
        return resp
    
    
    def sendEOF(self):
        return self.send(SC_ENDOFFILE)
    
    
    def sendExecude(self):
        return self.send(SC_EXECUTECOMMAND)
    
    
    def sendEndSession(self):
        return self.send(SC_ENDOFSESION)
    
    
    def sendWordsList(self, command):
        # send waiting one word
        print("lens is = ", "0x0" + str((len(command))))
        #self.send("0x0" + str((len(command))))
        self.send((len(command)))
        for t in command:
            # send command
            self.send(t)
    
    
    def execute(self, command):
        self.send(self.address)
        self.sendWordsList(command)
        #self.sendEOF()
        self.sendExecude()
        self.sendEndSession()
    
    
    # put in Stek
    
    
    
    



