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
        from model.commandmenu import CommandMenu
        self.menu = CommandMenu(key = 0) 
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

    def test_init_CommandMenu(self):# {{{
#         print(var.split(" "))
        self.assertEqual(
            len(self.menu.itemslist)
            , 1)
#         self.assertEqual(
#             self.commad.runtimeCommand() , None)
#         self.assertEqual(
#             self.commad.onEndCommand , None)
#         self.assertEqual(
#             self.commad.onStartCommand , None)
        # }}}

    def test_addItems(self):# {{{
        self.assertEqual(
            len(self.menu.itemslist)
            , 1)
        self.menu.addItems([10, 20])
        self.assertEqual(
            len(self.menu.itemslist)
            , 3)
        self.assertIsNotNone(self.menu.addItems((100, 200)))
        self.assertEqual(
            len(self.menu.itemslist)
            , 5)
        self.assertIsNotNone(self.menu.getItem(10))
        self.assertIsNotNone(self.menu.getItem(0))
        self.assertIsNotNone(self.menu.getItem(200))
        self.assertIsNone(self.menu.getItem(300))
        # }}}

    def test_addOneItem(self):# {{{
        self.assertEqual(
            len(self.menu.itemslist)
            , 1)
        self.menu.addOneItem(1)
        self.assertEqual(
            len(self.menu.itemslist)
            , 2)
        print(self.menu.itemslist)
        self.assertIsNotNone(self.menu.getItem(0))
        self.assertIsNotNone(self.menu.getItem(1))
        self.assertIsNone(self.menu.getItem(9))
        # }}}

    def test_runtime(self):# {{{
        self.assertNotEqual(self.menu.updatetime, 0)
        self.assertTrue(
            self.menu.runtime())
        self.assertFalse(
            self.menu.runtime())
        # }}}

    def test_reseTimer(self):# {{{
        self.assertNotEqual(self.menu.delayRunTime, 0)
        self.assertEqual(self.menu.updatetime, self.menu.reseTimer(0.3))
        # }}}

# }}}

if __name__ == "__main__":# {{{
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
# }}}