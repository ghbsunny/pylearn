#注意多了__repr__魔术函数的区别

class Item:
    def __init__(self,**kwargs):
        self.__spec=kwargs
    
    def __repr__(self):
        return str(sorted(self.__spec.items()))
myphone = Item(mark='Huawei',color='gold',memory='8G')

print(myphone)

class Item:
    def __init__(self,**kwargs):
        self.__spec=kwargs

mycar = Item(mark='Red Flag',color = 'black',year = 2019)

print(mycar)

class A:
    def __str__(self):
        return "__str__"
    def __repr__(self):
        return "__repr__"
a1 = A()
print(a1)
a1
