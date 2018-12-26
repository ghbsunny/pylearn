num = int(input("input a num: "))
line = num//2
print("first method")
if num%2 == 0:
    print("Your input num could not form an rhombus,it should be an odd num.")
else:
    for i in range(-line,line+1):
        print(' ' *(-i)+'*'*(num+2*i)) if i < 0 else print(' '*i + '*'*(num-2*i))
print()
print("second method")
for i in range(-line,line+1):
    print(" "*abs(i)+"*"*(num-2*abs(i)))
print()
print("third method")
for i in range(-line,line+1):
    if i < 0:
        print(' ' *(-i)+'*'*(num+2*i))
    else:
        print(' '*i + '*'*(num-2*i))
