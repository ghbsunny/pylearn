def cmd_dispatcher():
    cmds = {}
    
    def reg(command):
        def _reg(fn):
            cmds[command] = fn
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

@reg('boy')
def foo1():
    print("sunny")
@reg('nice')
def foo2():
    print("day")

dispatcher()

