import random

print("1 use normal method")
class RandomGen:
    def __init__(self,start,stop,count):
        self.start = start
        self.stop = stop
        self.count = count
    
    def generate(self):
        return [random.randint(self.start,self.stop) for x in range(self.count)]

a = RandomGen(1,100,7)
print(a.generate())

print()
print("2 use class method")

class RandomGen:
    def __init__(self,start,stop,count):
        self.start = start
        self.stop = stop
        self.count = count
    @classmethod
    def generate(cls,start=1,stop=100,count=3):
        return(random.randint(start,stop) for x in range(count))

a = RandomGen(1,10,2)
for x in a.generate():
    print(x)

print()
print("3 use generator method")

class RandomGenerator:
    def __init__(self,start=1,stop=100,patch=10):
        self.start = start
        self.stop = stop
        self.patch = patch
        self._gen = self._generate()

    def _generate(self):
        while True:
            yield random.randint(self.start,self.stop)
    
    def generate(self,count=0):
        if count <= 0:
            return [next(self._gen) for _ in range(self.patch)]
        else:
            return [next(self._gen) for _ in range(count)]
a = RandomGenerator()
print(a.generate())
print(a.generate(5))

print()
print("4 use another generator method")
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
a = RandomGenerator()
print(a.generate())
print(a.generate(5))

print()
print("5 use property method")
class RandomGenerator:
    def __init__(self,start=1,stop=100,patch=10):
        self.start = start
        self.stop = stop
        self._patch = patch
        self._gen = self._generate()
    def _generate(self):
        while True:
            yield [random.randint(self.start,self.stop) for _ in range(self.patch)]
    
    def generate(self):
        return next(self._gen)
    
    @property
    def patch(self):
        return self._patch
    
    @patch.setter
    def patch(self,value):
        self._patch = value

a = RandomGenerator()
print(a.generate())
a.patch = 3
print(a.generate())
