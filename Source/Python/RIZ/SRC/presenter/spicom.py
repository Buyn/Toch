import spidev


class SPICom(object):
    
    
    def __init__(self, address):
        self.address = address
        self.spi = spidev.SpiDev()
        self.spi.max_speed_hz = 18000000
        self.spi.mode = 0b00
        self.spi.lsbfirst = False



    
    def execute(self, command):
        pass
    
    
    # put in Stek
    
    
    
    



