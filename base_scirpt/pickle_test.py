import pickle
filename = "/tmp/test01"

x = 'a'
y = 100
z = '100'
m = {'a':x,'b':y,'c':z}

with open(filename,'wb') as f:
    pickle.dump(m,f)
    n = pickle.dumps(m)
    print(n,type(n))
        
with open(filename,'rb') as f:
    for _ in range(1):
        a = pickle.load(f)
        print(a,type(a))

x = ['a',
100,
['abc'],
{'a':1,'b':2,'c':3}]

lst = []

with open(filename,'wb') as f:
    for i in x:
        lst.append(pickle.dumps(i))
        
with open(filename,'rb') as f:
    for i in lst:
        a = pickle.loads(i)
        print(a,type(a))
