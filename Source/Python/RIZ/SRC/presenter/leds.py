from model.globalsvar import SC_SETSHIFTOUT
class LEDs(object):
    
    def __init__(self, spi):
        self.spi = spi
        self.bitWordLast = 0
        self.chenged = False

    
    def ledOn(self, ledpin):
        self.bitWordLast |= 1<<ledpin 
        self.chenged = True

    
    def send(self):
        if not self.chenged: return False
        self.spi.execute( [self.bitWordLast, SC_SETSHIFTOUT])
        self.chenged = False
        return True

    
    def ledOff(self, ledpin):
        self.bitWordLast ^= 1<<ledpin 
        self.chenged = True
    
    
    
    
    
    
    
    



