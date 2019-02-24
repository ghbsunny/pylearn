print("the code is an eg for decorator without parameter")
import datetime
import time

def logger(fn):
    def wrapper(*args,**kwargs):
        #before 功能增强
        print("args={},kwargs={}".format(args,kwargs))
        start = datetime.datetime.now()
        print("start time is {} ".format(start))
        ret = fn(*args,**kwargs)
        #after 功能增强
        duration = datetime.datetime.now() - start
        end = datetime.datetime.now()
        print("end time is {} ".format(end))
        print("function {} took {} s".format(fn.__name__,duration.total_seconds()))
        return ret
    return wrapper

@logger #相当于是add = logger(add)
def add(x,y,z=18):
    print("=============call add===========")
    time.sleep(2)
    return x+y+z

print("now result is {} ".format(add(3,y=12)))

print("----------------------------------------------")

print("the code is an eg for decorator with one parameter")
import datetime
import time

def copy_properties(src):
    def _copy(dest):
        dest.__name__ = src.__name__
        dest.__doc__ = src.__doc__
        return dest
    return _copy

def logger(duration, func = lambda name,duration:print(name + " func cost " + str(duration) + "s is too slow")):
    def _logger(fn):
        @copy_properties(fn) #wapper = wapper(fn)(wrapper)
        def wrapper(*args,**kwargs):
            """Here is wrapper doc"""
            #before 功能增强
            print("args={},kwargs={}".format(args,kwargs))
            start = datetime.datetime.now()
            print("start time is {} ".format(start))
            ret = fn(*args,**kwargs)
            #after 功能增强
            deltatime = (datetime.datetime.now() - start).total_seconds()
            if deltatime > duration:
                func(fn.__name__,duration)
            end = datetime.datetime.now()
            print("end time is {} ".format(end))
            print("function {} took {} s".format(fn.__name__,deltatime))
            return ret
        return wrapper
    return _logger

@logger(2) #相当于是add = logger(add)
def add(x,y,z=15):
    """This is add doc"""
    print("=============call add===========")
    time.sleep(2)
    return x+y+z

print("now result is {} name={},doc={}".format(add(3,y=12),add.__name__,add.__doc__))
