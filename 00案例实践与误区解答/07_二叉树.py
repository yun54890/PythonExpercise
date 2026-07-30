



class Node:
    def __init__(self,item=None):
        self.item = item
        self.lchild = None
        self.rchild = None

class BinaryTree:
    def __init__(self,root_node=None):
        self.root=root_node

    def add(self,item):
        new_node = Node(item)
        if self.root is None:
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

    def breadth(self):
        if self.root is None:
            return
        queue = []
        queue.append(self.root)
        while len(queue) != 0:
            node = queue.pop(0)
            print(node.item,end=" ")
            if node.lchild is not None:
                queue.append(node.lchild)
            if node.rchild is not None:
                queue.append(node.rchild)

    def preorder(self,root):
        if root is not None:
            print(root.item,end=" ")
            self.preorder(root.lchild)
            self.preorder(root.rchild)

    def inorder(self,root):
        if root is not None:
            self.inorder(root.lchild)
            print(root.item,end=" ")
            self.inorder(root.rchild)

    def postorder(self,root):
        if root is not None:
            self.postorder(root.lchild)
            self.postorder(root.rchild)
            print(root.item,end=" ")






if __name__=='__main__':
    tree = BinaryTree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.breadth()
    print()
    tree.preorder(tree.root)
    print()
    tree.inorder(tree.root)
    print()
    tree.postorder(tree.root)
