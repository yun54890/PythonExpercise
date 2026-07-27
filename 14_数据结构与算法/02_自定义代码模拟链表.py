"""
案例：自定义代码模拟链表

列表介绍：
    概述：
        它属于数据结构之 线性结构的一种, 每个节点都只能有 1个前驱 和 1个后驱节点
    作用：
        用于优化顺序表的弊端(如果没有足够的连续的内存空间,会导致扩容失败)
        链表扩容时, 有地儿就行, 连不连续无所谓
    组成：
        由 节点 组成, 其中节点由 元素域(数值域) 和 链接域(地址域)组成
    分类：
        根据 节点类型不同, 链表主要分为：
        单向链表:
        单向循环链表:
        双向链表:
        双向循环链表:
"""

# 自定义SinleNode类,  表示 节点
class SingleNode:
    def __init__(self,item):
        self.item = item
        self.next = None

# 自定义SingleLinkedList类, 表示 链表
class SingleLinkedList:
    def __init__(self,head=None,node=None):
        self.head = head

    #  链表是否为空
    def is_empty(self):
        # 思路：判断头节点是否为None,如果为None,则链表为空
        # if else
        # if self.head is None:
        #     return True
        # else:
        #     return False

        # 三元表达式
        # return True if self.head is None else False
        return self.head is None

    # 链表长度
    def length(self):
        # 创建游标(表示当前节点), 默认从头节点开始
        cur = self.head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    # 遍历整个链表
    def travel(self):
        # 创建游标(表示当前节点), 默认从头节点开始
        cur = self.head
        while cur is not None:
            print(cur.item)
            cur = cur.next


    # 链表头部添加元素
    def add(self):
        pass

    # 链表尾部添加元素
    def append(self):
        pass

    # 指定位置添加元素
    def insert(self):
        pass

    # 删除节点
    def remove(self):
        pass

    # 查找节点是否存在
    def search(self):
        pass





if __name__ == '__main__':
    # node1 = SingleNode(10)
    # print(f"元素域(数值域)：{node1.item}")
    # print(f"链接域(地址域)：{node1.next}")
    # print(f"node1对象：{node1}")               # 地址值
    # print(f"node1的类型:{type(node1)}")
    # print("-"*30)
    #
    # my_linkedlist = SingleLinkedList(node1)
    # print(f"头节点为:{my_linkedlist.head}")
    # print(f"头节点的元素域:{my_linkedlist.head.item}")
    # print(f"头节点的地址域:{my_linkedlist.head.next}")

    node1 = SingleNode('乔峰')
    my_list = SingleLinkedList(node1)
    # print(f'头节点为：{my_list.head}')
    # print(f'头节点的数值域:{my_list.head.item}')
    print("-"*30)
    print(my_list.is_empty())
    print("-"*30)
    print(my_list.length())
    my_list.travel()