'''
Created on 28 янв. 2019 г.

@author: BuYn
'''
import unittest
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
        self.ledstm = SPICom(LEDSTM_ADRRESS, debugmode=2)
        print("*"*33,i,"*"*33)


    def tearDown(self):
        i = "tear Down"
        print("*"*33,i,"*"*33)


    def testSpidevXref(self):
        self.assertEqual(
            self.ledstm.send( 200 )
            , 200 + 1)

        
    def testGetVar(self):
        self.assertEqual(
            self.ledstm.getVar( 100 )
            , SC_ENDOFSESION + 1)

        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
