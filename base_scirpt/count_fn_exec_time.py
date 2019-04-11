import time
import datetime
from functools import wraps

print("This program list five method to count one func exec time ")
#利用装饰器计算函数运行间隔时长
def timeit(fn):
    @wraps(fn)
    def wrapper(*args,**kwargs):
        start = datetime.datetime.now()
        ret = fn(*args,**kwargs)
        delta = (datetime.datetime.now() - start ).total_seconds()
        print("1 {} took {}s".format(fn.__name__,delta))
        return ret
    return wrapper

@timeit
def add(x,y):
    time.sleep(2)
    return x+y

print(1,add(4,6))

#利用上下文计算函数运行间隔时长

import datetime
class Timeit:
    def __init__(self,fn):
        self.fn = fn
    def __enter__(self):
        self.start = datetime.datetime.now()
        return self.fn
    
    def __exit__(self,exc_type,exc_val,exc_tb):
        delta = (datetime.datetime.now() - self.start).total_seconds()
        print("2 {} took {}s".format(self.fn.__name__,delta))

def newadd(x,y):
    time.sleep(2)
    return x+y

with Timeit(newadd) as fn:
    print(2,newadd(4,8))

#通过可调用对象实现
import datetime
class Timeit:
    def __init__(self,fn):
        self.fn = fn
    def __enter__(self):
        self.start = datetime.datetime.now()
        return self.fn
    
    def __exit__(self,exc_type,exc_val,exc_tb):
        delta = (datetime.datetime.now() - self.start).total_seconds()
        print("3 {} took {}s".format(self.fn.__name__,delta))
    
    def __call__(self,x,y):
        print(x,y)
        return self.fn(x,y)
    
def newadd(x,y):
    time.sleep(2)
    return x+y

with Timeit(newadd) as timeobj:
    print(3,timeobj(4,5))

#将类当作装饰器使用,并且注意函数属性的继承
import datetime
import time
from functools import wraps,update_wrapper
class Timeit:
    """This is Timeit Class doc"""
    def __init__(self,fn):
        self.fn = fn
        #self.__doc__ = fn.__doc__
        #update_wrapper(self,fn)
        wraps(fn)(self)
    
    def __call__(self,*args,**kwargs):
        self.start = datetime.datetime.now()
        ret = self.fn(*args,**kwargs)
        self.delta = (datetime.datetime.now()-self.start).total_seconds()
        print("4 {} took {}s call".format(self.fn.__name__,self.delta))
        return ret

@Timeit
def newadd(x,y):
    '''This is add function doc'''
    time.sleep(2)
    return x+y

print(4,newadd(3,2))
print(newadd.__doc__)
print(Timeit.__doc__)

#利用contextlib来实现
import contextlib
import datetime
import time

@contextlib.contextmanager
def add(x,y):
    start = datetime.datetime.now()
    try:
        yield x+y
    finally:
        delta = (datetime.datetime.now() - start).total_seconds()
        print("5 method 5 took {}".format(delta))

with add(4,17) as f:
    time.sleep(2)
    print(5,f)
