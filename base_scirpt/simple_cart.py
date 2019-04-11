#模拟购物车增加物品
class Color:
    RED = 0
    BLUE = 1
    GREEN = 2
    GOLDEN = 3
    BLACK = 4
    OTHER = 10000
    
class Item:
    def __init__(self,**kwargs):
        self.__spec=kwargs
    
    def __repr__(self):
        return str(sorted(self.__spec.items()))

class Cart:
    def __init__(self):
        self.items = []
    
    def additem(self,item:Item):
        self.items.append(item)
    
    def getallitems(self):
        return self.items

mycart = Cart()
myphone = Item(mark='Huawei',color=Color.GOLDEN,memory='8G')
mycart.additem(myphone)

mycar = Item(mark='Red Flag',color = Color.BLACK,year = 2019)
mycart.additem(mycar)

print(mycart.getallitems())
