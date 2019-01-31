print("first method")
for i in range(1,10):
    s = " "
    for j in range (1,10):
        if j < i+1:
            s += str(j) + "*" + str(i) + "=" + str(i*j) + ' '
    print(s)


print("second method")
for i in range(1,10):
    s = " "
    for j in range (1,i+1):
            s += str(j) + "*" + str(i) + "=" + str(i*j) + ' '
    print(s)


print("third method")
for i in range(1,10):
    for j in range(1,i+1):
        print(str(j) + '*' + str(i) + '=' + str(i*j),end = '\t')
    print()

print("The forth method,I think it is best")
for i in range(1,10):
    for j in range (1,i+1):
        print('{}*{}={}\t'.format(j,i,j*i),end="")
    print()

print("another methon")
for i in range(1,10):
    s =""
    for j in range (1,i+1):
        s += "{}*{}={:<4}".format(i,j,i*j)
    print("{:>72}".format(s))

print("different way to show 9*9,methon 1:")
for i in range(1,10):
    for j in range (i,10):
        print('{}*{}={}\t'.format(i,j,j*i),end="")
    print()


print("different way to show 9*9,methon 2:")
for i in range(1,10):
    s=' '*7*(i-1)
    for j in range (i,10):
        if i*j<10:
            s += str(i) + '*' + str(j) + '=' + str(i*j)+ "  "
        else:
             s += str(i) + '*' + str(j) + '=' + str(i*j)+ " "
    print(s)
for i in range(1,10):
    s =""
    for j in range (i,10):
        if j<4:
            s += "{}*{}={:<2} ".format(i,j,i*j)
        else:
            s += "{}*{}={:<3} ".format(i,j,i*j)
    print("{:>69}".format(s))
print("before is equal as below")
for i in range(1,10):
    s =""
    for j in range (i,10):
        s += "{}*{}={:<{}} ".format(i,j,i*j, 2 if j<4 else 3)
    print("{:>69}".format(s))

print("use list comprehension to print9*9")
[print("{}*{}={:<3}{}".format(j,i,i*j,'\n' if i==j else ' '),end="")for i in range(1,10) for j in range(1,i+1)]
[print("{}*{}={:<{}}{}".format(j,i,i*j,2 if i == 1 else 3,'\n' if i==j else ' '),end="")for i in range(1,10) for j in range(1,i+1)]
