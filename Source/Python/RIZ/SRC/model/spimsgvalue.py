class SPIMsgValue(object):
    
    def __init__(self, name, value):
        self.msg = {name:value}

    
    def set(self, msg):
        self.msg = msg

    
    def get(self):
        if len(self.msg) == 1:
            return self.msg
    
    
    
    


