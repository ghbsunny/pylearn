class Base:
    n = 0


class Point(Base):
    z = 6

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(self.x, self.y)

    def __getattr__(self, item):
        '''一个类的属性会按照继承关系找，如果找不到，就会执行__getattr__()方法，如果没有这个方法，就会
        抛出AttributeError异常表示找不到属性
        '''
        return "it is missing {}".format(item)

    def __setattr__(self, key, value):
        '''__setattr__方法可以拦截对实例属性的增加，修改操作，但是如果要设置生效，需要自己操作实例的__dict__'''
        print("setattr {} = {}".format(key, value))
        self.__dict__[key] = value

    # def __repr__(self):
    #     return "Point x={},y={}".format(self.x,self.y)

    def __delattr__(self, item):
        '''实例定义了特殊方法，阻止实例删除属性的方法，但是依然可以通过类删除属性,del Point.z'''
        print('Can not del {}'.format(item))

    def __getattribute__(self, item):
        #return item #报错，TypeError: 'str' object does not support item assignment
        #return self.__dict__[item]  #无限递归，RecursionError: maximum recursion depth exceeded
        return object.__getattribute__(self,item)



p1 = Point(4, 5)
print(p1.__dict__)
print(p1.x)
print(p1.y)
print(p1.z)
print(p1.t)
p1.x = 50
print(p1.__dict__)
print(Point.__dict__)
print(Point.z)
print(p1.x)
