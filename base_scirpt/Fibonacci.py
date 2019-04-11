# print the n number value in Fibonacci sequence
n = int(input("which number value you want to know: "))
f1 = 1
f2 = 1
for i in range(3,n+1):
    fi = f1+f2
    f1 = f2
    f2 = fi
print("The " + str(n) + "th number's value is "+ str(fi))

print()
#print all the number which is less than the number you have input
print("method 1")
n = int(input("Input the bigget number in Fibonacci sequence you want to show: "))
f1 = 1
f2 = 1
print(f1)
while f2 < n:
    print(f2)
    f1, f2 = f2, f1+f2 #f1=f2,f2 = f1+f2

print()
print("method 2")
n = int(input("Input the bigget number in Fibonacci sequence you want to show: "))
f1 = 1
f2 = 1
print(f1)
print(f2)
for i in range(1,n+1):
    if i == f1+f2: 
        print(i)
        f1 = f2
        f2 = i
print("--------------------------------")
import datetime
start = datetime.datetime.now()
pre = 0
cur = 1
print(cur,end=' ')
n=35
for i in range(n-1):
    pre,cur = cur,pre+cur
    print(cur,end=' ')
delta = (datetime.datetime.now()-start).total_seconds()
print()
print(delta)
print('--------------------------------')
import datetime
n=35
start = datetime.datetime.now()
def fib(n):
    return 1 if n<2 else fib(n-1)+fib(n-2)
for i in range(n):
    print(fib(i),end=' ')
    delta = (datetime.datetime.now()-start).total_seconds()
print()
print(delta)
print('--------------------------------')
import datetime
start = datetime.datetime.now()
pre = 0
cur = 1
print(cur,end=' ')
def fib(n,pre=0,cur=1):
    pre,cur=cur,pre+cur
    print(cur,end=' ')
    if n == 2:
        return
    fib(n-1,pre,cur)
fib(n)
delta = (datetime.datetime.now()-start).total_seconds()
print()
print(delta)
print('--------------------------------')
def fib():
    x = 0
    y = 1
    while True:
        yield y
        x,y = y,x+y
foo = fib()
for _ in range(5):
    print(next(foo))
print('----------------------------------')
pre = 0
cur = 1
print(cur,end=' ')
def fib1(n,pre=0,cur=1):
    pre,cur=cur,pre+cur
    print(cur,end=' ')
    if n == 2:
        return
    fib1(n-1,pre,cur)
fib1(5)
print()
print('----------------------------------')
import functools
@functools.lru_cache()
def fib(n):
    if n < 3:
        return 1
    return fib(n-1)+fib(n-2)
newfib = [fib(x) for x in range(35)]
print(newfib)
print('-------------Use Class-----------------')
class Fib:
    def __init__(self):
        self.items = [0,1,1]
    
    def __call__(self,index):       
        return self[index]
    
    def __iter__(self):
        return iter(self.items)
    
    def __len__(self):
        return len(self.items)
    
    def __getitem__(self,index):
        if index < 0:
            raise IndexError('Wrong Index')
            
        if index < len(self.items):
            return self.items[index]
        
        for i in range(len(self),index+1):
            self.items.append(self.items[i-1]+self.items[i-2])
        return self.items[index]
    
    def __str__(self):
        return str(self.items)
    
    __repr__ = __str__
    
fib = Fib()
print(fib(5),len(fib))
print(fib(7),len(fib))
for x in fib:
    print(x)

print(fib[5],fib[9])

