from enum import Enum, unique
from model.globalsvar import *
import pygame
from presenter.leds import LEDs

@unique
class State(Enum):# {{{
    SHARPENNING           	= 15
    POLISHING             	= 14
    MIDDLE_CYCLE           	= 13
    RIGHT_SIDE             	= 12
    LEFT_SIDE              	= 11
    CERAMIC_KNIFE          	= 10
    POLISHING_DISK_CLEANING	= 9 
    FULL_CYCLE             	= 8 
    READY                 	= 7
    NOTREADY                = 0
    
    @staticmethod
    def list():
        return list(map(lambda c: c.value, State))
    # }}}

@unique
class FuncList (Enum):# {{{
    RUNTIME           	= 0
    ONSTART            	= 1
    ONEND           	= 2

    @staticmethod
    def list():
        return list(map(lambda c: c.value, FuncList))
    # }}}

class CommandsMenu (Enum):# {{{
    def __init__(self, spi, buttons, leds):# {{{
        pass
#         for oneLine in State.
        # }}}
    # }}}

class LEDsMenu(object):
    
    def __init__(self, spi, buttons, leds):# {{{
        self.leds = LEDs(self.spi)
        self.spi = spi
        self.buttons = buttons
        self.leds = leds
        self.newState = 0
        self.oldState = 0
        self.state = 0
        self.runtimeCommand = self.notreadyState
        self.cheget = False
        pygame.mixer.init()
        pygame.mixer.music.set_volume(1.0)

    
    def runtime(self):
        if self.cheget:
            self.oldState = self.newState
            self.newState()
            self.cheget =False
        return self.runtimeCommand()

    
    def setRuntime(self, command):
        self.runtimeCommand = command 

    
    def readyState(self):
        self.leds.blink(self.state)
        return True

    def notreadyState(self):
        return False
    
    def setNewState(self, onChegeCommand):
        self.newState = onChegeCommand
        self.cheget = True

    
    def executeStatus(self):
        self.leds.ledTrig(self.state)
        if self.state == State.SHARPENNING.value:
#         set blue
            self.spi.execute([0x0A, 0xff, 0x00, 0x00, SC_LED01SET])
            self.spi.execute([0x0A, 0xff, 0x00, 0x00, SC_LED02SET])
            self.spi.execute([0x0A, 0xff, 0x00, 0x00, SC_LED03SET])
            pygame.mixer.music.load("ready.wav")
            pygame.mixer.music.play()
        if self.state == State.POLISHING_DISK_CLEANING.value:
#         set orange
            self.spi.execute([0x0A, 0x00, 0xff, 0xff, SC_LED01SET])
            self.spi.execute([0x0A, 0x00, 0xff, 0xff, SC_LED02SET])
            self.spi.execute([0x0A, 0x00, 0xff, 0xff, SC_LED03SET])
            pygame.mixer.music.load("ready.wav")
            pygame.mixer.music.play()
        if self.state == State.POLISHING.value or self.state == State.CERAMIC_KNIFE.value:
#         set Ylow
            self.spi.execute([0x0A, 0xff, 0x00, 0xff, SC_LED01SET])
            self.spi.execute([0x0A, 0xff, 0x00, 0xff, SC_LED02SET])
            self.spi.execute([0x0A, 0xff, 0x00, 0xff, SC_LED03SET])
            pygame.mixer.music.load("ready.wav")
            pygame.mixer.music.play()

    
    
    def setReadyState(self):
        self.cheget = False
        self.runtimeCommand = self.readyState
        self.state = State.READY.value
        pygame.mixer.music.load("ready.wav")
        pygame.mixer.music.play()
        self.spi.execute([SC_LEDSTART])
#         set green
        self.spi.execute([0x0A, 0x00, 0x00, 0xff, SC_LED01SET])
        self.spi.execute([0x0A, 0x00, 0x00, 0x00, SC_LED02SET])
#         set green
        self.spi.execute([0x0A, 0x00, 0x00, 0xff, SC_LED03SET])
        self.buttons.setComandOnPress(B_CHOICE, 
            lambda: print("B_CHOICE", self.nextStatus()))
        self.buttons.setComandOnPress(B_OK, 
            lambda: print("B_OK", self.executeStatus()))
        self.buttons.setComandOnPress(B_RESET, 
            lambda: print("B_RESET", self.setReadyState()))

    
    def nextStatus(self):
        if self.state == State.NOTREADY.value:
            self.state = State.READY.value
            return self.state 
        if self.state == State.SHARPENNING.value:
            self.state = State.READY.value + 1
            return self.state 
        self.state += 1
        return self.state 
    
    
    
        
    
    
    
    
    
    
    
    
    # }}}
    



