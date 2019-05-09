from model.globalsvar import *
# from presenter.spicom import SPICom
from model.typsconvert import *
class StepMotor(object):
    
    
    def __init__(self, spi):
#         self.spi = SPICom(LEDSTM_ADRRESS, debugmode=2)
        self.spi = spi

    
    def move(self, tag, steps):
        return self.spi.execute([isInt(steps), self.getTag(tag), SM_STEP])

    
    def getTag(self, tag):
        if isinstance(tag, int):
            return tag
        if isinstance(tag, str):
            tag = tag.capitalize()
            return StepMotorsList[tag].value
        raise ValueError('is not a valid type'.format(tag))

    
    def setSpeed(self, tag, steps):
        return self.spi.execute([isInt(steps), self.getTag(tag), SM_SPEED])
    
    def setEnable(self, tag, steps):
        return self.spi.execute([isInt(steps), self.getTag(tag), SM_ENABLE])
    
    
    def setDir(self, tag, steps):
        return self.spi.execute([isInt(steps), self.getTag(tag), SM_DIR])
    
    
    
    
    
    
    



