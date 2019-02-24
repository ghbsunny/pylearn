n = int(input("please input one num: "))
def func(n):
    return 1 if n == 1  else n*func(n-1)
result = func(n)
print(str(n)+"! result is " + str(result))
