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
#         self.spi = SPICom(LEDSTM_ADRRESS, debugmode=2)
#         self.leds= LEDs(self.spi)
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
        from model.commanditem import CommandItem
        self.commad = CommandItem(key = 0, 
                                  runtimeCommand = lambda : print("runtime"), 
                                  onStartCommand = None,
                                  onEndCommand   = None)
        # }}}

    def tearDown(self):# {{{
        i ="End Test Log"
        print("-++-"*10,i,"-++-"*33)
        i = "tear Down"
        print("-++-"*10,i,"-++-"*33)
        # }}}

    def test_init_CommandItem(self):# {{{
#         print(var.split(" "))
        self.assertEqual(
            self.commad.key
            , 0)
        self.assertEqual(
            self.commad.runtimeCommand() , None)
        self.assertEqual(
            self.commad.onEndCommand , None)
        self.assertEqual(
            self.commad.onStartCommand , None)
        # }}}
        
    def test_setergeter_CommandItem(self):# {{{
#         print(var.split(" "))
        self.assertEqual(
            self.commad.set_on_end_command(
                lambda x : x+1
                ) , None)
        self.assertEqual(
            self.commad.onEndCommand(10)
            , 11)
        self.commad.onStartCommand = lambda x : x+1
        self.assertEqual(
            self.commad.onStartCommand(20) , 21)
        # }}}
if __name__ == "__main__":# {{{
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
# }}}
# }}}
