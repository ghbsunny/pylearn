print("method 1")
source = {'a':{'b':1,'c':2},'d':{'e':3,'d':{'g':8}},'g':19}

def flatmap(src:dict,dest=None,prefix=''):
    if dest == None:
        dest = {}
    
    for k,v in src.items():
        if isinstance(v,(dict,tuple,set,dict)):
            flatmap(v,dest,prefix + k + '.')
        else:
            dest[prefix + k] = v
    
    return dest

print(flatmap(source))

print("---------------------------------------")
print("method 2")
source = {'a':{'b':1,'c':2},'d':{'e':3,'d':{'g':8}},'g':19}

def flatmap(src:dict):
    def _flatmap(src:dict,dest=None,prefix=''):

        for k,v in src.items():
            if isinstance(v,(dict,tuple,set,dict)):
                _flatmap(v,dest,prefix + k + '.')
            else:
                dest[prefix + k] = v
                
    dest = {}
    _flatmap(src,dest)

    return dest

print(flatmap(source))
