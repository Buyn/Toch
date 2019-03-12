

class DebugPrint(object):
    
    def __init__(self, startingdebugmod):
        self.debugmod = startingdebugmod

    
    def print(self, printonmod, *arg):
        if self.debugmod < printonmod: return 0
        print(*arg)
        return 1
    
    


