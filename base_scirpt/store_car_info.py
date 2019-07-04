class Car:
    def __init__(self,mark,color,price,speed):
        self.mark = mark
        self.color = color
        self.price = price
        self.speed = speed


class  CarInfo:
    def __init__(self):
        self.info = []
    
    def addcar(self,car:Car):
        self.info.append(car)
    
    def getall(self):
        return self.info

ci = CarInfo()
car = Car('audi','red',80,400)
ci.addcar(car)
car = Car('benzi','black',100,300)
ci.addcar(car)
a = ci.getall()
for x in a:
    print("{}'s color is {},its speed is {},sold for {} thousand".format(x.mark,x.color,x.speed,x.price))
