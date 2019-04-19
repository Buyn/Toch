from model.commanditem import *
from array import array


class CommandMenu(object):
    

    def reseTimer(self):
        pass
    
    
    def __init__(self, key=0):
        self.itemslist = {}
        self.addItems(key)
        self.updatetime = 0
        self.reseTimer()
        
    def addOneItem(self, key):
        if isinstance(key, int):
            result = CommandItem(key)
            self.itemslist.update({key : result})
            return result
        else : return None

    def addItems(self, key):
        if isinstance(key, int):
            return self.addOneItem(key)
        elif isinstance(key, list) or  isinstance(key, array) or isinstance(key, tuple):
            result = []
            for item in key:
                result.append(self.addOneItem(item))
            return result
        else  : return None
    
    def getItem(self, key):
        return self.itemslist.get(key, None)

    
    def runtime(self):
        return True
    
    

