'''# {{{
Created on 28 янв. 2019 г.

@author: BuYn
'''
# }}}
import unittest# {{{
from model.globalsvar import *
from presenter.spicom import SPICom
from veiw.termenu import TerMenu
import time
from presenter.leds import LEDs
# }}}
class Test(unittest.TestCase):# {{{

    @classmethod# {{{
    def setUpClass(self):
        print("*"*33,"*"*33)
        print("file opened")
        print("*"*33,"*"*33)
        self.spi = SPICom(LEDSTM_ADRRESS, debugmode=2)
        self.leds= LEDs(self.spi)
        # }}}
        
    @classmethod# {{{
    def tearDownClass(cls):
        print("*"*33,"*"*33)
        print("tear down module")
        print("*"*33,"*"*33)
        # }}}

    def setUp(self):# {{{
        i ="set up"
        print("-++-"*10,i,"-++-"*33)
        i ="Start Test Log"
        print("-++-"*10,i,"-++-"*33)
        self.terMenu = TerMenu(self.spi, self.leds)
        # }}}

    def tearDown(self):# {{{
        i ="End Test Log"
        print("-++-"*10,i,"-++-"*33)
        i = "tear Down"
        print("-++-"*10,i,"-++-"*33)
        # }}}

    def testisLedcommand(self):# {{{
        self.assertEqual(
            self.terMenu.isLEDCommand( "led set 1 2 3 4" )
            , False)
        self.assertEqual(
            self.terMenu.isLEDCommand( "ledstop" )
            , True)
        var = "debug 3"
        print(var.split(" "))
        self.assertEqual(
            self.terMenu.isCommandList( var.split(" "))
            , True)
        self.assertEqual(
            self.terMenu.isLEDCommand( "g" )
            , True)
        # }}}

    def testisCommandList(self):# {{{
        var = "debug 3"
        print(var.split(" "))
        self.assertEqual(
            self.terMenu.isCommandList( var.split(" "))
            , True)
        var = "led set 1 2 3 4"
        print(var.split(" "))
        self.assertEqual(
            self.terMenu.isCommandList( var.split(" "))
            , True)
        var = "debug 1"
        print(var.split(" "))
        self.assertEqual(
            self.terMenu.isCommandList( var.split(" "))
            , True)
        var = "ledstop"
        print(var.split(" "))
        self.assertEqual(
            self.terMenu.isCommandList( var.split(" ") )
            , False)
        # }}}
        
    def test_ledsend(self):# {{{
        var = "leds 8"
        print(var.split(" "))
        self.assertEqual(
            self.terMenu.isCommandList( var.split(" "))
            , True)
        self.assertEqual(
            self.leds.chenged , True)
        self.assertEqual(
            self.leds.bitWordLast , 256)

        # }}}
        
    def test_inputOn(self):# {{{
        self.assertEqual(
            self.terMenu.inputOn , True)
        self.terMenu.setInputPause(sec = 0.8) 
        self.assertEqual(
            self.terMenu.inputOn , True)
        self.terMenu.setInputPause(1)
        self.assertEqual(
            self.terMenu.inputOn , False)
        time.sleep(1)
        self.assertEqual(
            self.terMenu.setInputPause() , True)
        self.assertEqual(
            self.terMenu.inputOn , True)
        # }}}
        
    def test_inputOff(self):# {{{
        self.terMenu.inputOff = True
        self.assertEqual(
            self.terMenu.inputOn , True)
        self.terMenu.setInputPause(sec = 0.8) 
        self.assertEqual(
            self.terMenu.inputOn , True)
        self.terMenu.setInputPause(1)
        self.assertEqual(
            self.terMenu.inputOn , True)
        time.sleep(1)
        self.assertEqual(
            self.terMenu.setInputPause() , False)
        self.assertEqual(
            self.terMenu.inputOn , True)
        # }}}

        
if __name__ == "__main__":# {{{
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
# }}}
# }}}
