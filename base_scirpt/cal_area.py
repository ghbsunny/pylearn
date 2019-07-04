import math

class Shape:
    def area(self):
        raise NotImplementedError('基未未实现')

class Triangle(Shape):
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    
    @property
    def area(self):
        p = (self.a+self.b+self.c)/2
        return math.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))

class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height
        
    @property
    def area(self):
        return self.width*self.height

class Circle(Shape):
    def __init__(self,radius):
        self.d = radius * 2
    
    @property
    def area(self):
        return math.pi*self.d*self.d*0.25

shapes = [Triangle(3,4,5),Rectangle(3,4),Circle(4)]
for s in shapes:
    print('The area of {} = {}'.format(s.__class__.__name__,s.area))
