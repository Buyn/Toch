'''
Created on 28 янв. 2019 г.

@author: BuYn
'''
import unittest
import main
from model.globalsvar import *
from presenter.spicom import SPICom
from main import isLEDCommand, isCommandList

class Test(unittest.TestCase):


    @classmethod
    def setUpClass(self):
        print("*"*33,"*"*33)
        print ("file opened")
        print("*"*33,"*"*33)

        
    @classmethod
    def tearDownClass(cls):
        print("*"*33,"*"*33)
        print("tear down module")
        print("*"*33,"*"*33)


    def setUp(self):
        i ="set up"
        print("*"*33,i,"*"*33)


    def tearDown(self):
        i = "tear Down"
        print("*"*33,i,"*"*33)


    def testisLedcommand(self):
        self.assertEqual(
            isLEDCommand( "led set 1 2 3 4" )
            , False)
        self.assertEqual(
            isLEDCommand( "ledstop" )
            , True)


    def testisCommandList(self):
        var = "led set 1 2 3 4"
        print(var.split(" "))
        self.assertEqual(
            isCommandList( var.split(" "))
            , True)
        var = "ledstop"
        print(var.split(" "))
        self.assertEqual(
            isCommandList( var.split(" ") )
            , False)
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
