#print the number of prime in 100000
print("method 1")
n = 100000
count = 0
strs = ''
for c in range(2,n):
    for a in range(2,int(c**0.5+1)):
        if c%a == 0:
            break
    else:
            strs += str(c) + ' '
            count += 1
          #  break
print(count)
print(strs)
print()
print("method 2")
import datetime
start = datetime.datetime.now()
count = 0
sum = 0
strs = ''
#n = int(input("input a num,The program will calculate the number of prime in it : "))
for i in range(2,100000):
    for j in range (2,int(i**0.5+1)):
        sum  += 1
        if not i % j:
            break
    else:
        count += 1
        strs += str(i) + ' '
delta = (datetime.datetime.now()-start).total_seconds()
print(delta)
print("The number of prime is: ",count)
print("The number of traversal is: ",sum)
print(strs)

print()
print("method 3")
count = 1
strs = '2 '
for i in range(3,100001,2):
    if i>10 and i%10 == 5:
        continue
    else:
        for j in range(2,int(i**0.5+1)):
            if i%j == 0:
                break
        else:
            count += 1
            strs += str(i) + ' '
print(count)
print(strs)

print("--------------------------------")
import datetime
start = datetime.datetime.now()
count = 1
for x in range(3,100000,2):
    if x > 10 and x%10 == 5:
        continue
    for i in range(3,int(x ** 0.5) + 1,2):
        if x%i == 0:
            break
    else:
        count += 1
        pass
delta = (datetime.datetime.now() - start).total_seconds()
print(delta)
print(count)
print("-------------------------------------")

import datetime
start = datetime.datetime.now()
number = 100000
count = 2
for num in range(4,number):
    if num%6 != 1 and num%6 != 5:
        continue
    else:
        snum = int(num**0.5 + 1)
        for i in range(5,snum,2):
            if not num%i:
                break
        else:
            count +=1
            pass
delta = (datetime.datetime.now() - start).total_seconds()
print(delta)
print(count)
print("-------------------------------------")
