from functools import partial

class ClassMethod:
    def __init__(self,fn):
        self._fn = fn

    def __get__(self, instance, cls):
        ret = partial(self._fn,cls)
        return ret


class A:
    @ClassMethod
    def clsmtd(cls):
        print(cls.__name__)

print(A.__dict__)
print(A.clsmtd)
A.clsmtd()
