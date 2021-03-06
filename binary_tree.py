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


# 递归序
def recursion_order(node):
    if node is None:
        return

    print('第一次', node.value)
    recursion_order(node.left)
    print('第二次', node.value)
    recursion_order(node.right)
    print('第三次', node.value)


# 用递归实现先序遍历
def recursion_preorder(node):
    if node is None:
        return
    print('递归先序遍历', node.value)
    recursion_preorder(node.left)
    recursion_preorder(node.right)


# 用递归实现中序遍历
def recursion_inorder(node):
    if node is None:
        return
    recursion_inorder(node.left)
    print('递归中序遍历', node.value)
    recursion_inorder(node.right)


# 用递归实现后序遍历
def recursion_postorder(node):
    if node is None:
        return
    recursion_postorder(node.left)
    recursion_postorder(node.right)
    print('递归后序遍历', node.value)


# 用非递归方式实现先序遍历
def non_recursion_preorder(node):
    stack = [node]
    while len(stack) > 0:
        cur = stack.pop()
        print('非递归先序遍历', cur.value)
        if cur.right is not None:
            stack.append(cur.right)

        if cur.left is not None:
            stack.append(cur.left)


# 用非递归实现中序遍历
def non_recursion_inorder(node):
    stack = [node]
    cur = node
    while len(stack) > 0:
        while cur.left is not None:
            stack.append(cur.left)
            cur = cur.left

        cur2 = stack.pop()
        print('非递归中序遍历', cur2.value)
        if cur2.right is not None:
            stack.append(cur2.right)
            cur = cur2.right


# 用非递归实现后序遍历
def non_recursion_postorder(node):
    stack1 = [node]
    stack2 = []
    while len(stack1) > 0:
        cur = stack1.pop()
        stack2.append(cur)
        if cur.left is not None:
            stack1.append(cur.left)

        if cur.right is not None:
            stack1.append(cur.right)

    while len(stack2) > 0:
        cur = stack2.pop()
        print('非递归后序遍历', cur.value)


head = init_node()
recursion_order(head)
recursion_preorder(head)
recursion_inorder(head)
recursion_postorder(head)

non_recursion_preorder(head)
non_recursion_inorder(head)
non_recursion_postorder(head)















