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
