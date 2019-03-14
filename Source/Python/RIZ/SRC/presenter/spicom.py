#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import spidev
from model.globalsvar import * 
import time
from veiw.debugprint import DebugPrint


class SPICom(object):
    
    
    def __init__(self, address, debugmode = DEBUGMODE):
        self.address = address
        self.debugmode = debugmode
        self.dp = DebugPrint(debugmode)
        self.spi = spidev.SpiDev()


    def send(self, word):
        if (self.debugmode >= 3): print("sending = [ ", word, " ] ")
        self.spi.open(BUS,DEVICE)
        self.spi.max_speed_hz = 18000000
        self.spi.mode = 0b00
        self.spi.lsbfirst = False
        resp = self.spi.xfer([word])
        self.spi.close()
        if (self.debugmode >= 3): print("send = [ ", word, " ] , resiv = [ ", resp, " ]")
        time.sleep (SPI_SLEEPAFTERSEND);
        return resp
    
    
    def sendEOF(self):
        if (self.debugmode >= 2): print("send = [ END OF FILE ] ")
        return self.send(SC_ENDOFFILE)
    
    
    def sendExecude(self):
        if (self.debugmode >= 2): print("send = [ EXECUTE LAST ONE COMMAND ] ")
        return self.send(SC_EXECUTECOMMAND)
    
    
    def sendEndSession(self):
        if (self.debugmode >= 2): print("send = [ END OF SISION ] ")
        return self.send(SC_ENDOFSESION)
    
    
    def sendWordsList(self, command, testmsg = None):

        result = []
        # send waiting one word
        if (self.debugmode >= 3): print("comad list = ",  command)
        if (self.debugmode >= 3): print("lens is = ", "0x0" + str((len(command))))
        self.send((len(command)))
        for t in command:
            # send command
            result.append(self.send(t))
        return result
    
    
    def sendGetVar(self):
        return self.send(SC_GETVARBYNAME)
    
    
    def decodeError(self, error):
        if (error == 0): return " ok [ NO ERROR ]"
        elif (error == DISINHRONERROR): return " [ DISINHRONERROR ]"
        elif (error == DISINHRONADRESSERROR): return " [ DISINHRONADRESSERROR ]"
        elif (error == STAKERRORCOMAND): return " [ STAKERRORCOMAND ]"
        elif (error == TIMEOUTSESION): return " [ TIMEOUTSESION ]"
        elif (error == SC_ENDOFSESION): return " ok [ SC_ENDOFSESION ]"
        return "Unknowe error code : " + str(error)
    

    def execute(self, command):
        if (self.debugmode >= 2): print("Sending to Adress = ", hex(self.address))
        if (self.debugmode >= 2): 
            print("Last Sesion Ends whith = ",
                      self.decodeError(self.send(self.address)))
        resivlist = self.sendWordsList(command)
        if (self.debugmode >= 2): print("MsgStakList elements waiting = ", resivlist[0]) 
        resivlist.append((self.sendExecude()))
        if (self.debugmode >= 2): print("commandStak send = ", command) 
        if (self.debugmode >= 2): print("commandStak resiv = ", resivlist) 
        if (self.debugmode >= 2): 
            print("Last command result = ",
                      self.decodeError(self.sendEndSession()))
            
            
    def getVar(self, varName):
        if (self.debugmode >= 2): print("Sending to Adress = ", hex(self.address))
        if (self.debugmode >= 2): 
            print("Last Sesion Ends whith = ",
                      self.decodeError(self.send(self.address)))
        resivlist = self.sendWordsList([varName])
        if (self.debugmode >= 2): print("MsgStakList elements waiting = ", resivlist[0]) 
        resivlist.append((self.sendGetVar()))
        if (self.debugmode >= 2): print("commandStak send = ", 1, varName) 
        if (self.debugmode >= 2): print("commandStak resiv = ", resivlist) 
        if (self.debugmode >= 2): print("MsgStakList elements waiting = ", resivlist[0]) 
        if (self.debugmode >= 2): print("Send Var Name = ", varName)
        if (self.debugmode >= 2): print("SPI get Name = ", self.sendGetVar())
        return self.sendEndSession()

    
    def sendIsMsgWating(self):
        if (self.debugmode >= 2): print("send = [ IS MESAGES WATING ] ")
        return self.send(SC_ISMSGWATING)
    

    def sendGetMsgByCount(self):
        if (self.debugmode >= 2): print("send = [ GET MESAGES BY COUNT] ")
        return self.send(SC_GETMSGBYCOUNT)
    
    
    def getAllMsg(self, testmsg=None):
        if (self.debugmode >= 2): print("Sending to Adress = ", hex(self.address))
        if (self.debugmode >= 2): 
            print("Last Sesion Ends whith = ",
                      self.decodeError(self.send(self.address)))
        resivlist = self.sendIsMsgWating()
        if testmsg == 0 :
            resivlist = self.send(0)
        if resivlist == 0 :
            if (self.debugmode >= 2): print("No Mesages") 
            self.sendEndSession()
            return 0
        if (self.debugmode >= 2): print("MsgStakList elements waiting = ", resivlist) 
        msglist = []
        sendmsg = resivlist
        for t in range(resivlist):
            msglist.append(self.send(sendmsg))
            sendmsg = t
        if (self.debugmode >= 2): print("resiv mesages list = ", msglist)
        self.sendEndSession()
        return msglist 

    
    def startSesion(self):
        if (self.debugmode >= 2): print("Sending to Adress = ", hex(self.address))
        if (self.debugmode >= 2): 
            print("Last Sesion Ends whith = ",
                      self.decodeError(self.send(self.address)))

    
    def isWaitingMsg(self, testmsg = 0):
        self.startSesion()
        self.isAdressCorrect(   self.sendIsMsgWating())
        return                  self.sendEndSession()

    
    def isAdressCorrect(self, resiv):
        if (self.debugmode >= 2): 
            print(
                "We Sending to ", 
                "" if resiv == self.address 
                    else "in", "correct Adress")
    
    
    def getOneMsg(self, number, testmsg = 0):
        self.startSesion() 
        self.isAdressCorrect(self.sendGetMsgByCount())
#             print("Sending Namber of values we wating = ", hex(number))
        self.dp(2, "Sending Namber of values we wating = ", hex(number))
        resiv = [self.send(number)]
        self.dp(2, "Resivid value whith name= ", resiv[0])
        resiv.append(self.sendEndSession())
        self.dp(2, "We Get", resiv)
        return resiv