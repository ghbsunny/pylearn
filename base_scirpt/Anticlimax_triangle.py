#print Anticlimax triangle
num = int(input("input an odd num: "))
line = num//2
print("first method")
if num%2 == 0:
    print("Your input num should be an odd num.")
else:
    for i in range(-line,line+1):
        print(' ' *(line+i)+'*'*(1-2*i)) if i < 0 else print(' '*(line-i) + '*'*(2*i+1))
print("second method")
if num%2 == 0:
    print("Your input num should be an odd num.")
else:
    for i in range(-line,line+1):
        c=abs(i)
        print(' '*(line-c)+'*'*(c*2+1))
