print("一般字段类型检查")
class Person:
    def __init__(self,name:str,age:int):
        params =((name,str),(age,int))
        if not self.checkdata(params):
            raise TypeError()

        self.name = name
        self.age =age

    def checkdata(self,params):
        for p,t in params:
            print(p)
            print(t)
            if not isinstance(p,t):
                return False
        return True

p = Person('sunny',30)

print("*"*30)
print("使用描述器，函数装饰器，写入实例属性的时候做检查")
class Typed:
    def __init__(self,name,type):
        self.name = name
        self.type = type

    def __get__(self, instance, owner):
        if instance is not None:
            return instance.__dict__[self.name]
        return self

    def __set__(self, instance, value):
        if not isinstance(value,self.type):
            raise TypeError(value)
        instance.__dict__[self.name] = value

import inspect
def typeassert(cls):
    params = inspect.signature(cls).parameters
    print(params)
    for name,param in params.items():
        print(param.name,param.annotation)
        if param.annotation != param.empty:
            setattr(cls,name,Typed(name,param.annotation))
    return cls

@typeassert
class Person:
    def __init__(self,name:str,age:int):
        self.name = name
        self.age = age

    def __repr__(self):
        return "{} is {}".format(self.name,self.age)

p = Person('tom',20)
print(p)


print("*"*30)
print("使用描述器，将函数装饰器改成类装饰器，写入实例属性的时候做检查")
class Typed:
    def __init__(self,name,type):
        self.name = name
        self.type = type

    def __get__(self, instance, owner):
        if instance is not None:
            return instance.__dict__[self.name]
        return self

    def __set__(self, instance, value):
        print("T.set",self,instance,value)
        if not isinstance(value,self.type):
            raise ValueError(value)

import inspect
class TypeAssert:
    def __init__(self,cls):
        self.cls = cls #记录被包装的Person类
        params = inspect.signature(cls).parameters
        print(params)
        for name,param in params.items():
            print(param.name,param.annotation)
            if param.annotation != param.empty:
                setattr(self.cls,name,Typed(name,param.annotation)) #注入类属性
        print(self.cls.__dict__)
    def __call__(self,name,age):
        p = self.cls(name,age)
        return p

@TypeAssert
class Person:
    def __init__(self,name:str,age:int):
        self.name = name
        self.age = age


p = Person('tom',20)
print(p)
