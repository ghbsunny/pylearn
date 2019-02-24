print("method 1")
a = 1
for i in range(9):
    a=(a+1)*2
print(a)
print("method 2")
a=1
t=0
while True:
    t += 1
    if t == 10:
        break
    a = (a+1)*2
print(a)
def monkey(n):
    if n == 1:
        return 1
    return 2 *( monkey(n-1) + 1)
peach = monkey(10)
print(peach)
print('----------------------------')
def peach(days=10):
    if days == 1:
        return 1
    return (peach(days-1)+1)*2
print(peach(10))
