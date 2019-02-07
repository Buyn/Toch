# RPi PINOUTS{{{
# MOSI -> GPIO10
# MISO -> GPIO9
# SCK  -> GPIO11
# CE1  -> GPIO7
# CE1  -> GPIO8
# }}}

# get the GPIO Library and SPI Library{{{
import spidev
import time
# }}}

BUS = 0 
DEVICE = 0
#Initialze the SPI # {{{
spi = spidev.SpiDev()
# }}}

#Varialbes for the Debounce # {{{

# }}}

#End of the Script
def writeNumber(value):
    # create spi object
    # open spi port 0, device (CS) 1
    spi.open(BUS,DEVICE)
    spi.writebytes(value)
    spi.close()
    return -1

def sendOn():
    # create spi object
    # open spi port 0, device (CS) 1
    spi.open(BUS,DEVICE)
    resp = spi.xfer([0x31,0x30,0X0A])
    spi.close()
    return -1

def sendOff():
    # create spi object
    # open spi port 0, device (CS) 1
    spi.open(BUS,DEVICE)
    resp = spi.xfer([0x31,0x31,0X0A])
    spi.close()
    return -1

def readNumber():
    # number = bus.read_byte_data(address, 1)
    number = 0 
    #number = spi.readbytes(1)
    return number

while True:
    var = input("Enter 1 - 9: ")
    if not var:
        continue

    if  var == 1:
        sendOn()

    if  var == 0:
        sendOff()

    #writeNumber(var)
    print "RPI: Hi Arduino, I sent you ", var
    # sleep one second
    time.sleep(1)

    number = readNumber()
    print "Arduino: Hey RPI, I received a digit ", number
    print
