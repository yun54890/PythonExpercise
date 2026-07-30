from platform import node


# 定义Node类, 表示二叉树的节点
class Node:
    def __init__(self,item):
        self.item = item        # 元素域：即：节点存储的数据
        self.lchild = None      # 左子节点
        self.rchild = None      # 右子节点



# 自定义BinaryTree类, 表示二叉树
class BinaryTree:
    def __init__(self,Node=None):
        self.root = Node       # 根节点, 类似于：链表的 self.head 头节点

    # 添加节点
    def add(self,item):
        new_node = Node(item)
        if self.root == None:
            self.root = new_node
            return
        queue = []
        queue.append(self.root)
        while True:
            node = queue.pop(0)
            if node.lchild is None:
                node.lchild = new_node
                return
            else:
                queue.append(node.lchild)

            if node.rchild is None:
                node.rchild = new_node
                return
            else:
                queue.append(node.rchild)

    # 广度优先遍历
    def breadth(self):
        pass

    # 深度优先(前)
    def preorder(self):
        pass

    # 深度优先(中)
    def inorder(self):
        pass

    # 深度优先(后)
    def postorder(self):
        pass



def dm01_test():
    # 创建节点
    node1 = Node('A')
    print(node1.item)
    print(node1.lchild)
    print(node1.rchild)
    print("-" * 30)

    bt = BinaryTree(node1)
    print(bt.root)
    print(bt.root.item)

# 模拟队列
def dm02_test():
    queue = []
    queue.append('A')
    queue.append('B')
    queue.append('C')
    queue.append('D')

    print(queue.pop(0))
    print(queue)


if __name__ == '__main__':
    # dm01_test()
    # dm02_test()
    bt = BinaryTree()
    bt.add("A")
    bt.add("B")
    bt.add("C")
    bt.add("D")
    bt.add("E")
