class StaticMethod:
    def __init__(self,fn):
        self._fn = fn

    def __get__(self, instance, owner):
        return self._fn

class A:
    @StaticMethod
    def stmtd():
        print('static method')

A.stmtd()
print(A.__dict__)
A().stmtd()
