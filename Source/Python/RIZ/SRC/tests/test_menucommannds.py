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
from model.commanditem import CommandItem
from model.commandmenu import CommandMenu
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
        self.commad = CommandItem(key = 0) 
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
            self.commad.runtimeCommand(None) , None)
#         self.assertEqual(
#             self.commad.onEndCommand , self.commad.passDef)
#         self.assertEqual(
#             self.commad.onStartCommand , self.commad.passDef)
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
        self.commad.set_runtime_command(self.runtimeTest, 0.3)
        self.assertEqual(self.commad.updatetime, 0)
        print("delay = ", self.commad.delayRunTime)
        print("next = ", self.commad.updatetime)
        print("time = ", time.time())
        self.assertEqual( self.commad.runtime(1), 11)
        print("next = ", self.commad.updatetime)
        print("time = ", time.time())
        self.assertIsNone( self.commad.runtime(2))
        time.sleep(0.5)
        print("next = ", self.commad.updatetime)
        print("time = ", time.time())
        self.assertEqual( self.commad.runtime(3), 13)
        print("next = ", self.commad.updatetime)
        print("time = ", time.time())
        self.assertIsNone(
            self.commad.runtime(4))
        self.assertIsNotNone(
            self.menu.setRunTimeCommand(
                0, self.runtimeTest, 0.3))
        self.assertIsNotNone(
            self.menu.addOneItem(1))
        self.assertIsNotNone(
            self.menu.setRunTimeCommand(
                1, self.runtimeTest02, 0.3))
        self.assertEqual( self.menu.runtime(1), 11)
        self.assertEqual( self.menu.runtime(22), 122)
        self.assertIsNone( self.menu.runtime(2))
        time.sleep(0.5)
        self.assertEqual( self.menu.runtime(3), 13)
        self.assertEqual( self.menu.runtime(33), 133)
        self.assertIsNone( self.menu.runtime(4))
        # }}}


    def test_setruntime(self):# {{{
        self.assertEqual(len(self.menu.runtimeList), 0)
        self.assertIsNotNone(self.menu.setRunTimeCommand( key = 0 , command = self.runtimeTest , timeout  = 0.3))
        self.assertEqual(len(self.menu.runtimeList), 1)
        self.assertIsNone(self.menu.setRunTimeCommand( key = 1 , command = self.runtimeTest , timeout  = 0.3))
        self.assertEqual(len(self.menu.runtimeList), 1)
        # }}}


    def runtimeTest(self,value):
        return value + 10
    
    
    def runtimeTest02(self,value):
        return value + 100
    
    
    def setTest01(self,value):
        return value + 10
    
    
    def setTest02(self,value):
        return value + 100
    
    
    def test_reseTimer(self):# {{{
        start = self.commad.updatetime
        self.commad.set_runtime_command(self.runtimeTest, 0.3)
        self.assertEqual(
            0.3
            , self.commad.delayRunTime)
        self.assertEqual(start, 
                            self.commad.updatetime)
        self.commad.reseTimer()
        self.assertNotEqual(start, 
                            self.commad.updatetime)
        # }}}

# }}}

    def test_switchActive(self):# {{{
        self.assertEqual(self.menu.activeItem, 0)
        self.menu.addItems(1)
        self.menu.addItems(3)
        self.assertIsNotNone(
            self.menu.switchActiv(1))
        self.assertIsNone(
            self.menu.switchActiv(10))
        self.assertEqual(self.menu.activeItem, 1)
        # }}}

# }}}

if __name__ == "__main__":# {{{
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
# }}}