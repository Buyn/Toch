'''
Created on 28 янв. 2019 г.

@author: BuYn
'''
import unittest
import main
from model.globalsvar import *
from presenter.spicom import SPICom

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
        print("-++-"*10,i,"-++-"*33)
        i ="Start Test Log"
        print("-++-"*10,i,"-++-"*33)


    def tearDown(self):
        i ="End Test Log"
        print("-++-"*10,i,"-++-"*33)
        i = "tear Down"
        print("-++-"*10,i,"-++-"*33)


    def testInpitLoop(self):
        var = "debug 3"
#         isCommandList( var.split(" "))
#         self.assertEqual(
#             main.inputLoop(1)
#             , 255)
#         var = "debug 1"
#         isCommandList( var.split(" "))
#         self.assertEqual(
#             main.inputLoop(10)
#             , 255)
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
