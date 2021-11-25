# 二叉树的遍历
class Node:
    # 定一个二叉树类
    value = None
    left = None
    right = None

    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def add_left(self, left):
        self.left = left

    def add_right(self, right):
        self.right = right


# 初始化二叉树的方法
def init_node():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node2.add_left(node4)
    node2.add_right(node5)
    node3.add_left(node6)
    node3.add_right(node7)
    node1.add_left(node2)
    node1.add_right(node3)

    return node1


# 初始化一个二叉树
head = init_node()
