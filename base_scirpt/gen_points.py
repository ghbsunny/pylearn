import random

class RandomGenerator:
    def __init__(self,start=1,stop=100,patch=10):
        self.start = start
        self.stop = stop
        self.patch = patch
        self._gen = self._generate()

    def _generate(self):
        while True:
            yield [random.randint(self.start,self.stop) for _ in range(self.patch)]
    
    def generate(self,count=0):
        if count > 0:
            self.patch = count
        return next(self._gen)
    
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

points = [Point(x,y) for x,y in zip(RandomGenerator().generate(5),RandomGenerator().generate(5))]

for p in points:
    print('{}:{}'.format(p.x,p.y))
