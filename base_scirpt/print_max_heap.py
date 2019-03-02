import math
def print_tree(array):
    index = 1
    depth = math.ceil(math.log2(len(array)))# 因为将待排序的第一位补了无用的0，如果不补0，这里为math.ceil(math.log2(len(array)+1))
    sep = '  '
    for i in range(depth):
        offset = 2 ** i
        print(sep * (2 ** (depth -i-1)-1),end='')
        line = array[index:index+offset]
        for j,x in enumerate(line):
            print("{:^{}}".format(x,len(sep)),end='')
            interval = 0 if i==0 else 2**(depth-i)-1
            if j < len(line)-1:
                print(sep*interval,end='')
        index += offset
        print()
        
#Heap Sort
#注意，为了让编码对应，索引号和值对应，在待排序的列表前加一个0
origin = [0,30,20,10,80,40,50,60,70,90,13,18,19,52]
total = len(origin)-1
print(origin)
print_tree(origin)
print("="*50)

# 调整当前节点
def heap_adjust(n,i,array:list):
    """
    假设调整节点的起点在n//2,保证所有调整的节点都有孩子节点
    n 是待比较的个数
    i 是当前节点的下标
    array 是待排序的数据
    """
    while 2*i <=n:
        lchild_index = 2*i
        max_child_index = lchild_index
        if n >lchild_index and array[lchild_index+1] > array[lchild_index]:
            max_child_index = lchild_index+1
        #和子树的节点比较
        if array[max_child_index] > array[i]:
            array[i],array[max_child_index] = array[max_child_index],array[i]
            i = max_child_index
        else:
            break

#构建大顶堆，大根堆
def max_heap(total,array:list):
    for i in range(total//2,0,-1):
        heap_adjust(total,i,array)
    return array

print_tree(max_heap(total,origin))
print("="*50)

#排序

def sort(total,array:list):
    while total >1:
        array[1],array[total] = array[total],array[1] # 堆顶和最后一个结点交换
        total -= 1
        if total ==2 and array[total] > array[total -1]:
            break
        heap_adjust(total,1,array)
    return array

print(origin)
print_tree(sort(total,origin))

