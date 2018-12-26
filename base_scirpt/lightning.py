num = int(input("input an odd num: "))
line = num//2
if num%2 == 0:
    print("Your input num should be an odd num.")
else:
    for i in range(-line,line+1):
        if i < 0:
            print(' '*(-i)+'*'*(line+i+1)) 
        elif i == 0:
            print('*'*num)
        else:
            print(' '*line + (line-i+1)*'*')
