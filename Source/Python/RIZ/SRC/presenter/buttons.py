'''
Created on 28 янв. 2019 г.

@author: BuYn
import test.test_buttons
'''

class Buttons(object):
    
    def __init__(self):
        self.change     = False
        self.lastBitWord= 0
        self.bReset     = 1
        self.bOk        = 1
        self.bChoice    = 1
        self.presed     = []

    
    def set(self, newBits):
        if self.lastBitWord == newBits: return False
        self.lastBitWord = newBits
        self.presed = []
        self.change = True
        for i in range (8):
            if newBits >> i&1 :
                self.presed.append(i)
    
    
    
    



