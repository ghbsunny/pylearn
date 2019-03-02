import math

def print_tree(array,unit_width=2):
    """
    居中对齐方案实现
    """
    length = len(array)
    depth = math.ceil(math.log2(length+1))
    index = 0
    width = 2**depth -1
    for i in range(depth):
        for j in range(2**i):
            print('{:^{}}'.format(array[index],width*unit_width),end =' '*unit_width)
            index += 1
            if index >=length:
                break
        width = width // 2
        print()
print_tree([x+1 for x in range(31)])

print('--------------method 2---------------')
def print_tree2(array):
    """
    使用投影栏格实现
    """
    index = 1
    depth = math.ceil(math.log2(len(array)+1))
    sep = '  '
    for i in range(depth):
        offset = 2**i
        print(sep * (2**(depth-i-1) - 1),end='')
        line = array[index:index+offset]
        for j,x in enumerate(line):
            print('{:^{}}'.format(x,len(sep)),end='')
            interval = 0 if i==0 else 2**(depth - i) -1
            if j <len(line) - 1:
                print(sep * interval,end='')
        index += offset
        print()
print_tree2([30,20,10,80,40,50,60,70,90,13,18,19,52])
