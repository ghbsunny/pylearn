print("regular traingle")
def show(n):
    tail = " ".join([str(i) for i in range(n,0,-1)])
    width = len(tail)
    for i in range(1,n):
        print("{:>{}}".format(" ".join([str(j) for j in range(i,0,-1)]),width))
    print(tail)
show(12)
print("Inverted triangle")
def showtail(n):
    tail = " ".join([str(i) for i in range(n,0,-1)])
    print(tail)
    for i in range(len(tail)):
        if tail[i] == " ":
            print(" "*i,tail[i+1:])
showtail(12)
