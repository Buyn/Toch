
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
import time
import sys
from model.globalsvar import * 
from presenter.spicom import SPICom
# }}}

#Initialze the SPI # {{{
ledstm = SPICom(LEDSTM_ADRRESS)
# }}}

#Varialbes for the Debounce # {{{

# }}}
    

def writeNumber(number):
    print ("RPI: Hi Arduino, I sent you ", number)
    number = ledstm.send(number)
    print ("Arduino: Hey RPI, I received a digit ", number)
    print
    return number


def sth(param0):
    return hex(int(param0))


def ledcommand(elm_var):
    if (elm_var[1] == "set"):
        print("Set led = ", 
              SC_LEDSET, 
              sth(elm_var[2]), 
              sth(elm_var[3]), 
              sth(elm_var[4]), 
              sth(elm_var[5]))
        ledstm.execute([SC_LEDSET, 
                      sth(elm_var[2]), 
                      sth(elm_var[3]), 
                      sth(elm_var[4]), 
                      sth(elm_var[5])]) 
    if (elm_var[1] == "01"):
        print("Set led 01 = ", 
              SC_LED01SET, 
              sth(elm_var[2]), 
              sth(elm_var[3]), 
              sth(elm_var[4]), 
              sth(elm_var[5]))
        ledstm.execute([SC_LED01SET, 
                      sth(elm_var[2]), 
                      sth(elm_var[3]), 
                      sth(elm_var[4]), 
                      sth(elm_var[5])]) 
    if (elm_var[1] == "02"):
        print("Set led 02 = ", 
              SC_LED02SET, 
              sth(elm_var[2]), 
              sth(elm_var[3]), 
              sth(elm_var[4]), 
              sth(elm_var[5]))
        ledstm.execute([SC_LED02SET, 
                      sth(elm_var[2]), 
                      sth(elm_var[3]), 
                      sth(elm_var[4]), 
                      sth(elm_var[5])]) 


def isInt(var):
    try:
        return int(var)
    except ValueError:
        print("Not know Command or number")
        return 0


def mainlope():
    while True:
        var = input("Enter Command: ")
        if not var:
            continue
        if  var == "ledstart":
            print ("Start LED")
            ledstm.execute([SC_LEDSTART])
            continue
        if  var == "ledstop":
            print ("Stop LED")
            ledstm.execute([SC_LEDSTOP])
            continue
        if  var == "t":
            print ("Test")
            ledstm.execute([0xf0, 0xf1, 0x01, 0x0f, SC_LEDSET])
            continue
        if  var == "b":
            print ("Blue")
            ledstm.execute([0xff, 0xf1, 0x01, 0x0f, SC_LEDSET])
            continue
        if  var == "r":
            print ("Red")
            ledstm.execute([0x00, 0xff, 0x00, 0x0f, SC_LEDSET])
            continue
        if  var == "g":
            print ("Green")
            ledstm.execute([0xf0, 0xf1, 0x01, 0x0f, SC_LEDSET])
            continue
        if  var == "w":
            print ("White")
            ledstm.execute([0xff, 0xff, 0xff, 0x0f, SC_LEDSET])
            continue
        if  var == "o":
            print ("OFF")
            ledstm.execute([0x00, 0x00, 0x00, 0x0f, SC_LEDSET])
            continue
        elm_var = None
        elm_var = var.split(' ')
        if (len(elm_var)>1):
            if (elm_var[0] == 'led'):
                ledcommand(elm_var)
            continue
        number = writeNumber(isInt(var))


if __name__ == '__main__':
    try:
        mainlope()
    except KeyboardInterrupt:
        sys.exit(0)
