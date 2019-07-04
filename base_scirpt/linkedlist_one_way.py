class SingleNode: #节点保存和下一跳
    def __init__(self,item,next=None):
        self.item = item
        self.next = next

    def __repr__(self):
        return "{} => {}" .format(self.item,self.next.item if self.next else None) #返回当前和下一个点的链条结构
        # return "{} => {}" .format(self.item,self.next) #返回从当前点开始的剩余完整的链条结构

class LinkList:
    """list实现链表
    默认情况下,只有节点知道自己的下一跳是谁，先直接访问某一个节点只能遍历，
    使用list,方便随机的访问某一个节点
    """
    def __init__(self):
        """初始化第一个节点和最后一个节点"""
        self.head = None
        self.tail = None
        self.items = []

    def append(self,item):
        node = SingleNode(item)
        if self.head is None:
            self.head = node #设置开头节点
        else:
            self.tail.next = node #当前最后一个节点关联下一跳
        self.tail = node #更新结尾节点

        self.items.append(node)
        return self

    def iternodes(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def getitem(self,index):
        return self.items[index]

ll = LinkList()
ll.append('abc')
ll.append(1).append(2).append(3)
ll.append('def')

print(ll.head)
print(ll.tail)

for item in ll.iternodes():
    if item == None:
        break
    print(item)

# for i in range(len(ll.items)):
#     print(ll.getitem(i))
