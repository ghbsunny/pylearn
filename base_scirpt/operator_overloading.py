#解决运算符重载出现的问题，以下主要是解决add，iadd和radd的问题
class A:
    def __init__(self,x):
        self.x = x

    def __add__(self, other):
        print(self,'add')
        try:
            x = other.x
            return self.x + other.x
        except AttributeError:
            try:
                x = int(other)
            except:
                x = 0
            return self.x +x

    def __iadd__(self, other):
        print(self,'iadd')
        return A(self.x + other.x)

    def __radd__(self, other):
        print(self,'radd')
        try:
            x = other.x
            return self.x + other.x
        except AttributeError:
            try:
                x = int(other)
            except:
                x = 0
            return self.x +x

class B:
    def __init__(self,x):
        self.x = x

a = A(4)
b = B(10)
print(a+b)
print(b+a)
print(1+a)
print(a+1)
print(a+'abc')
print('abc' + a)
