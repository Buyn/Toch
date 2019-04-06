from enum import Enum, unique
from model.globalsvar import SC_LEDSTOP, SC_LEDSTART
import pygame

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
        return True

    def notreadyState(self):
        return False
    
    def setNewState(self, onChegeCommand):
        self.newState = onChegeCommand
        self.cheget = True

    
    def setReadyState(self):
        self.runtimeCommand = self.readyState
        self.state = State.READY.value
        pygame.mixer.music.load("ready.wav")
        pygame.mixer.music.play()
        self.spi.execute([SC_LEDSTART])
        self.spi.execute([SC_LEDSTART])
    
    
        
    
    
    
    
    
    
    
    
    # }}}
    



