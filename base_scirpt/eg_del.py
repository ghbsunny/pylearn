#当引用计数器为0时，会自动调用__del__函数
#python实现了垃圾回收机制，不能确定对象何时执行垃圾回收
#垃圾回收对象销毁时，才会真正清理对象，还会再之前自动调用__del__方法
import time
class Person:
    def __init__(self,name,age =18):
        self.name = name 
        self.__age = age
    def __del__(self):
        print('now delete {}'.format(self.name))

def test():
    tom = Person('tom')
    tom.__del__()
    tom.__del__()
    tom.__del__()
    tom.__del__()
    print('=========== start ============')
    tom2 = tom
    tom3 = tom2
    print(1,'del tom1')
    del tom
    time.sleep(3)
    
    print(2,'del tom2')
    del tom2
    time.sleep(3)
    
    print('---------------------')
    print(3,'del tom3')
    del tom3
    time.sleep(3)
    print('=========== end ============')

test()
    
