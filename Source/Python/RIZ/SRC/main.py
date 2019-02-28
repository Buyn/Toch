#!/usr/bin/env python
# -*- coding: utf-8 -*- 
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
from array import array
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
ledstm = SPICom(LEDSTM_ADRRESS, debugmode=2)
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
    return hex(isInt(param0))


def fillLEDset(setlist, command):
    """Filling list from arrey and adding command"""
    return [
          isInt(setlist[5]),
          isInt(setlist[4]), 
          isInt(setlist[3]), 
          isInt(setlist[2]), 
          command 
          ] 
    

def ledcommand(elm_var):
    if (elm_var[1] == "set"):
        print("Set led  = ", 
                fillLEDset(elm_var, hex(SC_LEDSET)))
        ledstm.execute( fillLEDset(elm_var, SC_LEDSET))
    if (elm_var[1] == "01"):
        print("Set led 01 = ", 
                fillLEDset(elm_var, hex(SC_LED01SET)))
        ledstm.execute( fillLEDset(elm_var, SC_LED01SET))
    if (elm_var[1] == "02"):
        print("Set led 02 = ", 
                fillLEDset(elm_var, hex(SC_LED02SET)))
        ledstm.execute( fillLEDset(elm_var, SC_LED02SET)) 


def isInt(var):
    try:
        return int(var)
    except ValueError:
        print("Not know Command or number")
        return 0


def getUserInput():
    pass


def printHelp():
    """on h printing hel to log"""
    print ( "ledstart "," Start LED")
    print (  "ledstop ", "Stop LED")
    print (  "t ", "Test")
    print (  "b ", "Blue")
    print (  "r ", "Red")
    print (  "g ", "Green")
    print (  "w ", "White")
    print (  "o ", "OFF")
    print ( 'led ', "set", " red green blue speed  ", "Set led  = ")
    print ( 'led ', "01" , " red green blue speed  ", "Set led 01 = ") 
    print ( 'led ', "02" , " red green blue speed  ", "Set led 02 = ") 
    print ( 'debug ', "paramMode" , " set debug mode to new value") 


def isLEDCommand(var):
    if  var == "ledstart":
        print ("Start LED")
        ledstm.execute([SC_LEDSTART])
        return True
    if  var == "ledstop":
        print ("Stop LED")
        ledstm.execute([SC_LEDSTOP])
        return True
    if  var == "t":
        print ("Test")
        ledstm.execute([0x0f, 0x01, 0xf1, 0xf0, SC_LEDSET])
        return True
    if  var == "b":
        print ("Blue")
        ledstm.execute([0x0f, 0x00, 0x00, 0xff, SC_LEDSET])
        return True
    if  var == "r":
        print ("Red")
        ledstm.execute([0x0f, 0x00, 0xff, 0x00, SC_LEDSET])
        return True
    if  var == "g":
        print ("Green")
        ledstm.execute([0x0f, 0xff, 0x00, 0x00, SC_LEDSET])
        return True
    if  var == "w":
        print ("White")
        ledstm.execute([0x0f, 0xff, 0xff, 0xff, SC_LEDSET])
        return True
    if  var == "o":
        print ("OFF")
        return True
        ledstm.execute([0x0f, 0x00, 0x00, 0x00, SC_LEDSET])
    if  var == "h":
        printHelp()
        return True
    return False


def debugcommand(elm_var):
    ledstm.debugmode = isInt(elm_var[1])
    print("Debug mode set to ", elm_var[1])


def isCommandList(elm_var):
    if (not isinstance(elm_var, str) and len(elm_var) > 1):
#   if (len(elm_var)>1):
        if (elm_var[0] == 'led'):
            ledcommand(elm_var)
        if (elm_var[0] == 'debug'):
            debugcommand(elm_var)
        return True
    return False


def mainlope():
    while True:
        print ("Enter h for help(list of command)")
        var = input("Enter Command: ")
        if not var:
            continue
        if isLEDCommand(var): continue
        if isCommandList(var.split(' ')): continue
        number = writeNumber(isInt(var))


if __name__ == '__main__':
    try:
        mainlope()
    except KeyboardInterrupt:
        sys.exit(0)
