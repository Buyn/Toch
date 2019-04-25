from model.commanditem import *
from array import array


class CommandMenu(object):
    
    def __init__(self, key=0):
        self.itemslist = {}
        self.addItems(key)
        self.runtimeList = []
        self.activeItem = key
        

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

    
    def runtime(self, value = None):
        for item in self.runtimeList:
            if not item.runtime(value) == None :
                return item.lastreturn
        return None

    
    def setRunTimeCommand(self, key , command  , timeout ):
#         item = CommandItem()
        item = self.getItem(
            key)
        if not item:
            return None
        else:
            item.set_runtime_command(
                    command, timeout)
            self.runtimeList.append(item)
            return item

    
    def switchActiv(self, key):
        item = self.getItem(key)
        if item == None:# {{{
            return None
        else:
            self.activeItem = key
            return item
            # }}}
    
    
    

    
    
    
    
    

