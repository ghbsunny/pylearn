print("method 1:use if else to exchange num and sort")
a = int(input("input num1: "))
b = int(input("input num2: "))
c = int(input("input num3: "))
x=0
y=0
z=0
if a>=b:
    x = a
    y = b
else:
    x = b
    y = a
if x >= c:
    if c >= y:
        print(x,c,y)
    else:
        print(x,y,c)
else:
    print(c,x,y)
print('-----------------------------------')
print("use max")
nums = []
for i in range(3):
    nums.append(int(input('{}: '.format(i))))
sortnums = []
for m in range(3):
    b = max(nums)
    sortnums.append(b)
    nums.remove(b)
print(sortnums)
print('-------------------------------------')
print('use sort')
nums = []
for i in range(3):
    nums.append(int(input('{}: '.format(i))))
print(nums)
nums.sort()
print(nums)
nums.reverse()
print(nums)
