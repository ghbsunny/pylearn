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
