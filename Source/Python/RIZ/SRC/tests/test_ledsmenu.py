'''# {{{
Created on 28 янв. 2019 г.

@author: BuYn
'''# }}}
# {{{
import unittest
from model.globalsvar import *
from presenter.spicom import SPICom
from model.spimsg import SpiMSG
from presenter.leds import LEDs
import time
from presenter.buttons import Buttons
from veiw.ledsMenu import *
# }}}



class Test(unittest.TestCase):

    @classmethod# {{{
    def setUpClass(self):
        print("*"*33,"*"*33)
        print ("file opened")
        print("*"*33,"*"*33)
        self.spi = SPICom(LEDSTM_ADRRESS, debugmode=4)
        self.buttons = Buttons()
        self.leds = LEDs(self.spi)
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
        self.ledsMenu = LEDsMenu(
                            spi     = self.spi, 
                            buttons = self.buttons,
                            leds    = self.leds 
                            )
        # }}}

    def tearDown(self):# {{{
        i ="End Test Log"
        print("-++-"*10,i,"-++-"*33)
        i = "tear Down"
        print("-++-"*10,i,"-++-"*33)
        # }}}


    def test_init(self):# {{{
        self.assertEqual(
            State.NOTREADY.value , 0)
        self.assertEqual(
            self.ledsMenu.newState , 0)
        self.assertEqual(
            self.ledsMenu.oldState , 0)
#         self.assertEqual(
#             self.ledsMenu.state.getkey("") , 0)
        # }}}
        
    def test_runtime(self):# {{{
        self.ledsMenu.setRuntime(self.ledsMenu.readyState)
        self.assertEqual(
            self.ledsMenu.runtime() , True)
        self.assertEqual(
            self.ledsMenu.cheget , False)
        self.ledsMenu.setNewState(self.ledsMenu.setReadyState)
        self.assertEqual(
            self.ledsMenu.cheget , True)
        print(State.list())
        # }}}

if __name__ == "__main__":# {{{
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
# }}}
