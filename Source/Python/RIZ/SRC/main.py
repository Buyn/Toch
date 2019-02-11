
# Bitbang'd SPI interface with an MCP3008 ADC device{{{
# MCP3008 is 8-channel 10-bit analog to digital converter
#  Connections are:
#     CLK => SCLK  
#     DOUT =>  MISO
#     DIN => MOSI
#     CS => CE0
# RPi PINOUTS
# MOSI -> GPIO10
# MISO -> GPIO9
# SCK  -> GPIO11
# CE1  -> GPIO7
# CE1  -> GPIO8
'''
Created on 10 февр. 2019 г.
@author: BuYn
'''
# }}}

# get the GPIO Library and SPI Library{{{
import spidev
import time
import sys
from model.globalsvar import * 
from presenter.spicom import SPICom
# }}}

#Initialze the SPI # {{{
spi = spidev.SpiDev()
ledstm = SPICom(LEDSTM_ADRRESS)
# }}}

#Varialbes for the Debounce # {{{

# }}}

def buildReadCommand(channel):
    startBit = 0x01
    singleEnded = 0x08

    # Return python list of 3 bytes
    #   Build a python list using [1, 2, 3]
    #   First byte is the start bit
    #   Second byte contains single ended along with channel #
    #   3rd byte is 0
    return []
    
def processAdcValue(result):
    '''Take in result as array of three bytes. 
       Return the two lowest bits of the 2nd byte and
       all of the third byte'''
    pass
        
def readAdc(channel):
    if ((channel > 7) or (channel < 0)):
        return -1
    r = spi.xfer2(buildReadCommand(channel))
    return processAdcValue(r)
        

def writeNumber(value):
    # create spi object
    # open spi port 0, device (CS) 1
    spi.open(BUS,DEVICE)
    spi.writebytes([hex(int(value))])
    spi.close()
    return -1

def sendOn():
    # create spi object
    # open spi port 0, device (CS) 1
    spi.open(BUS,DEVICE)
    spi.max_speed_hz = 18000000
    spi.mode = 0b00
    spi.lsbfirst = False
    resp = spi.xfer([0x31])
    resp = spi.xfer([0x41])
    resp = spi.xfer([0x51])
    #resp = spi.xfer([0x31,0x30,0X0A])
    spi.close()
    return resp

def sendOff():
    # create spi object
    # open spi port 0, device (CS) 1
    spi.open(BUS,DEVICE)
    spi.max_speed_hz = 18000000
    spi.mode = 0b00
    spi.lsbfirst = False
    resp = spi.xfer([0x32])
    #resp = spi.xfer([0x32,0x33,0X0A])
    spi.close()
    return resp

def readNumber():
    # number = bus.read_byte_data(address, 1)
    number = 0 
    number = spi.readbytes(1)
    return number

def mainlope():
    while True:
        var = input("Enter Command: ")
        if not var:
            continue
        if  var == 1:
            print ("ON")
            print (sendOn())
        if  var == 0:
            print ("OFF")
            print (sendOff())
        if  var == "c":
            print ("Command")
            continue
        if  var == "led01":
            print ("set Led line to 01")
            ledstm.execute([C_LED_01])
            continue
        if  var == "t":
            print ("Test")
            ledstm.execute([C_LED_01, 0x01, 0x0f])
            continue
        writeNumber(var)
        print ("RPI: Hi Arduino, I sent you ", var)
        # sleep one second
        number = readNumber()
        print ("Arduino: Hey RPI, I received a digit ", number)
        print
        #value = getUserInput()
        #sendDade = ProcidCommands(value)
        #sendings(sendDate)
        #resiving()
        #printingResult()
        #val = readAdc(0)
        #print "ADC Result: ", str(val)
        #time.sleep(1)


if __name__ == '__main__':
    try:
        mainlope()
    except KeyboardInterrupt:
        spi.close() 
        sys.exit(0)