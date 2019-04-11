#该段代码实现了华氏温度，开氏稳定，摄氏温度之间的转换
#带华氏温度和开氏温度统一转换成摄氏温度进行换算
class Temperature:
    def __init__(self,t,unit='c'):
        self._c = None
        self._f = None
        self._k = None
        #将单位都转换位摄氏度，以后访问再计算其他单位的温度值
        if unit == 'k':
            self._k = t
            self._c = self.k2c(t)
        elif unit == 'f':
            self._f = t
            self._c = self.f2c(t)
        else:
            self._c = t
    
    #获取已知的温度值
    @property
    def c(self):
        return self._c
    @property
    def k(self):
        if self._k is None:
            self._k = self.c2k(self._c)
        return self._k
    @property
    def f(self):
        if self._f is None:
            self._f = self.c2f(self._c)
        return self._f
    
    #温度转换
    @classmethod
    def c2f(cls,c):
        return 9*c/5 + 32
    
    @classmethod
    def f2c(cls,f):
        return 5*(f-32)/9
    
    @classmethod
    def c2k(cls,c):
        return c+273.15
    
    @classmethod
    def k2c(cls,k):
        return k - 273.15
    
    @classmethod
    def f2k(cls,f):
        return cls.c2k(cls.f2c(f))
    
    @classmethod
    def k2f(cls,k):
        return cls.c2f(cls.k2c(k))

print(Temperature.c2f(40))
print(Temperature.c2k(40))
print(Temperature.f2c(104.0))
print(Temperature.k2c(313.15))
print(Temperature.k2f(313.15))
print(Temperature.f2k(104))

t = Temperature(40)
print(t.c,t.k,t.f)

t = Temperature(313.15,'k')
print(t.c,t.k,t.f)

t = Temperature(104,'f')
print(t.c,t.k,t.f)
