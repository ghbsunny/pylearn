from functools import partial
def cmd_dispatcher():
    """ 
    这个命令分发器，允许带参数，如foo1带两个参数，foo2不带参数
    """
    cmds = {}
    
    def reg(command,*args,**kwargs):
        def _reg(fn):
            func = partial(fn,*args,**kwargs)
            cmds[command] = func
            return fn
        return _reg
   
    def dispatcher():
        def default_func():
            print("unknow command")

        while True:
            cmd = input(">>>").strip()
            if cmd == "quit":
                break
            else:
                cmds.get(cmd,default_func)()
    return reg,dispatcher
reg,dispatcher = cmd_dispatcher()

@reg('boy',20,170)
def foo1(x,y):
    print("sunny is {} years old,is {} cm".format(x,y))
@reg('nice')
def foo2():
    print("day")

dispatcher()

