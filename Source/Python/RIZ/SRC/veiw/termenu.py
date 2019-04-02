#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# Menu Class with commads in termenal{{{
'''
Created on 10 февр. 2019 г.
@author: BuYn
'''
# }}}
# get Library {{{
from array import array
import pygame
import time
import sys
from model.globalsvar import * 
from veiw.debugprint import DebugPrint
# }}}

class TerMenu(object):# {{{

    def __init__(self, spi, debugmode = DEBUGMODE):# {{{
        self.dp = DebugPrint(debugmode)
        self.spi = spi
        self.inputOn = True
        self.pauseEnd = 0
        self.inputOff = False 
        # }}}

    def writeNumber(self, number):# {{{
        print ("RPI: Hi Arduino, I sent you ", number)
        number =self.spi.send(number)
        print ("Arduino: Hey RPI, I received a digit ", number)
        print
        return number
        # }}}

    def sth(self, param0):# {{{
        return hex(self.isInt(param0))
        # }}}

    def fillLEDset(self, setlist, command):# {{{
        """Filling list from arrey and adding command"""
        return [
              self.isInt(setlist[5]),
              self.isInt(setlist[4]), 
              self.isInt(setlist[3]), 
              self.isInt(setlist[2]), 
              command 
              ] 
        # }}}

    def ledcommand(self, elm_var):# {{{
        if (elm_var[1] == "set"):
            print("Set led  = ", 
                    self.fillLEDset(elm_var, hex(SC_LEDSET)))
            self.spi.execute( self.fillLEDset(elm_var, SC_LEDSET))
        if (elm_var[1] == "01"):
            print("Set led 01 = ", 
                    self.fillLEDset(elm_var, hex(SC_LED01SET)))
            self.spi.execute( self.fillLEDset(elm_var, SC_LED01SET))
        if (elm_var[1] == "02"):
            print("Set led 02 = ", 
                    self.fillLEDset(elm_var, hex(SC_LED02SET)))
            self.spi.execute( self.fillLEDset(elm_var, SC_LED02SET)) 
        # }}}

    def isInt(self, var):# {{{
        if isinstance(var, int):
            return var
        if isinstance(var, list) and len(var) == 1:
            return var[0]
        try:
            return int(var)
        except ValueError:
            print("Not know Command or number")
            return 0
        # }}}

    def getUserInput(self):# {{{
        while True:
            print ("Enter h for help(list of command)")
            var = input("Enter Command: ")
#             if not var:
#                 continue
            return var
        # }}}

    def printHelp(self):# {{{
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
        print ( 'im '   , " isWaitingMsg") 
        print ( 'gm '   , " getOneMsg") 
        print ( 'rd  = ready ', " To ready Status") 
        # }}}

    def setReadyStatus(self):# {{{
        pygame.mixer.init()
        pygame.mixer.music.load("file.wav")
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.play()
        # }}}

    def isLEDCommand(self, var):# {{{
        if  var == "ledstart":
            print ("Start LED")
            self.spi.execute([SC_LEDSTART])
            return True
        if  var == "ledstop":
            print ("Stop LED")
            self.spi.execute([SC_LEDSTOP])
            return True
        if  var == "t":
            print ("Test")
            self.spi.execute([0x0f, 0x01, 0xf1, 0xf0, SC_LEDSET])
            return True
        if  var == "b":
            print ("Blue")
            self.spi.execute([0x0f, 0x00, 0x00, 0xff, SC_LEDSET])
            return True
        if  var == "r":
            print ("Red")
            self.spi.execute([0x0f, 0x00, 0xff, 0x00, SC_LEDSET])
            return True
        if  var == "g":
            print ("Green")
            self.spi.execute([0x0f, 0xff, 0x00, 0x00, SC_LEDSET])
            return True
        if  var == "w":
            print ("White")
            self.spi.execute([0x0f, 0xff, 0xff, 0xff, SC_LEDSET])
            return True
        if  var == "o":
            print ("OFF")
            self.spi.execute([0x0f, 0x00, 0x00, 0x00, SC_LEDSET])
            return True
        if  var == "i":
            print ("Input loop Start")
            self.setInputPause(sec = 35)
            return True
        if  var == "h":
            self.printHelp()
            return True
        if  var == "im":
            print( self.spi.isWaitingMsg())
            return True
        if  var == "gm":
            print( self.spi.getOneMsg(0))
            return True
        if  var == "rd":
            print("To ready Status")
            self.setReadyStatus()
            return True
        return False
        # }}}

    def debugcommand(self, elm_var):# {{{
        self.spi.dp(self.isInt(elm_var[1]))
        print("Debug mode set to ", elm_var[1])
        # }}}

    def isCommandList(self, elm_var):# {{{
        if (not isinstance(elm_var, str) and len(elm_var) > 1):
            if (elm_var[0] == 'led'):
                self.ledcommand(elm_var)
            if (elm_var[0] == 'debug'):
                self.debugcommand(elm_var)
            return True
        return False
        # }}}

    def pruntMenu(self):# {{{
        if not self.setInputPause(): return False
        var = self.getUserInput()
        if var == None or var == "": return False
        if self.isLEDCommand(var): return True
        if self.isCommandList(var.split(' ')): return True
        return self.writeNumber(self.isInt(var))
        # }}}
    
    def setInputPause(self, sec = None):
        if self.inputOff: return False
        timenow = time.time()
        if sec == None and self.pauseEnd > timenow: 
            return False
        if sec == None and self.pauseEnd < timenow: 
            self.inputOn = True
            return True
        if isinstance(sec, int):
            self.pauseEnd = timenow + sec
            self.inputOn = False
    
    
# }}}





