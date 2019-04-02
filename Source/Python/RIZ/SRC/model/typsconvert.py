
def sth( param0):# {{{
    return hex(self.isInt(param0))
    # }}}
    

def isInt(var):# {{{
    if isinstance(var, int):
        return var
    if isinstance(var, list) and len(var) == 1:
        return var[0]
    try:
        return int(var)
    except ValueError:
        print("Not know Command or number")
        return 0
    # }}}
