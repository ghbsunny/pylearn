"""
双向链表，实现append,insert,pop,remove等方法
"""
class SingleNode: #节点保存和下一跳
    def __init__(self,item,prev=None,next=None):
        self.item = item
        self.next = next
        self.prev = prev

    def __repr__(self):
        '''返回上一节点 《==》当前节点 《==》下一个点的链条结构'''
        return "{} <=> {} <=> {}" .format(
                                          self.prev.item if self.prev else None,
                                          self.item,
                                          self.next.item if self.next else None)


class LinkList:
    def __init__(self):
        """初始化第一个节点和最后一个节点"""
        self.head = None
        self.tail = None
        self.size = 0

    def append(self,item):
        """尾部增加"""
        node = SingleNode(item)
        if self.head is None:
            self.head = node #设置开头节点
        else:
            self.tail.next = node #当前最后一个节点关联下一跳，新增的节点node为当前尾巴节点的下一个
            node.prev = self.tail #前后关联，当前尾巴变成新增节点node的上一个
        self.tail = node #更新结尾节点
        return self

    def insert(self,index,item):
        if index < 0:
            raise IndexError('Not negative index {}'.format(index))

        current = None
        for i,node in enumerate(self.iternodes()):
            if i == index: #找到index,在找到的index点进行插入
                current = node
                break
        else:  #没有找到，则在尾部进行追加
            self.append(item)
            return
        #找到index，开始执行如下代码
        node = SingleNode(item)
        prev = current.prev
        next = current

        if prev is None: #插入节点是首位
            self.head = node
        else:
            prev.next = node
            node.prev = prev
        node.next = next
        next.prev = node

    def pop(self):
        if self.tail is None:
            raise Exception('Empty')

        node = self.tail
        item = node.item
        prev = node.prev
        if prev is None: #表示当前链表只有一个节点
            self.head = None
            self.tail = None
        else:
            prev.next = None
            self.tail = prev
        return item

    def remove(self,index):
        if self.tail is None:  #表示当前链表是空
            raise Exception('Empty link')
        if index < 0:
            raise IndexError('Not negative index {}'.format(index))

        current = None
        for i,node in enumerate(self.iternodes()):
            if i == index:
                current = node
                break
        else:
            raise IndexError('Wrong index {}'.format(index))

        prev = current.prev
        next = current.next

        #要移除的节点可能在4种情况，分别处理
        if prev is None and next is None: #只有一个节点
            self.head = None
            self.tail = None
        elif prev is None:#移除的节点在头部
            next.prev = None #将原来的首部设置为None,如果原来的首部要任然可见，那么这里代码为self.head = next
            self.head = next
        elif next is None: # 移除的节点在尾部
            prev.next = None
            self.tail =prev
        else: #移除的节点在中间
            prev.next = next
            next.prev = prev
        del current

    def iternodes(self,reverse=False):
        """reverse 决定了当前链表是正常还是反向，方向决定了哪个值是头部或尾部"""
        current = self.tail if reverse else self.head
        while current:
            yield current
            current = current.prev if reverse else current.next


ll = LinkList()
ll.append('abc')
ll.append(1).append(2).append(3)
ll.append('def')
ll.append('5')

print(ll.head)
print(ll.tail)

for item in ll.iternodes():
    if item == None:
        break
    print(item)

print("======================================")
ll.remove(0)
for item in ll.iternodes():
    print(item)

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
ll.insert(3,9)
ll.insert(20,'sunny')
ll.insert(0,0)
ll.insert(1,10)
for item in ll.iternodes():
    print(item)



