'''
Created on 28 янв. 2019 г.

@author: BuYn
'''
import unittest
from model.globalsvar import *
from model import spimsgvalue

class Test(unittest.TestCase):


    @classmethod
    def setUpClass(self):
        print("*"*33,"*"*33)
        print ("Seting up class")
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


    def testInit(self):
        self.spimsg = spimsgvalue.SPIMsgValue(200, 100) 
        self.assertEqual(
            self.spimsg.msg.get(200)
            , 100)
        self.assertEqual(
            list(self.spimsg.msg.keys())[0]
            , 200)
        
        
    def testSetVariblsByValueNames(self):
        spimsg = spimsgvalue.SPIMsgValue(200, 100) 
        self.assertEqual( spimsg.msg , {200:100})
        spimsg.set({300:500}),
        self.assertEqual( spimsg.msg, {300:500})
        self.assertEqual( spimsg.get(), {300:500})
#         self.assertEqual(
#             list(spimsg.msg.keys())[0]
#             , 200)
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
