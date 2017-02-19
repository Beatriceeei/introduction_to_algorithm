# -*- coding:utf8 -*-

class Node():
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

def create_tree():
    # node1 = Node(2)
    # node2 = Node(5)
    # node3 = Node(4,node1,node2)
    # node4 = Node(8)
    # node5 = Node(7, None, node4)
    # root = Node(6,node3,node5)
    # return root
    node1 = Node(5)
    node2 = Node(6,node1)
    node3 = Node(8)
    node4 = Node(7,node2,node3)
    node5 = Node(5,None,node4)
    node6 = Node(2,None,node5)
    return node6

def recursive_inorder_tree_walk(node):
    if node is not None:
        recursive_inorder_tree_walk(node.left)
        print node.val
        recursive_inorder_tree_walk(node.right)

# root = create_tree()
# recursive_inorder_tree_walk(root)

# 使用栈的非递归中序遍历
def nonrecursive_inorder_tree_walk(root):
    shed = []
    node = root
    while node != None or shed:
        # 左子树有值一直压栈
        while node!=None:
            shed.append(node)
            node = node.left
        # 如果栈有值,弹出顶层元素,继续压右子树
        if shed:
            node = shed.pop(-1)
            print node.val
            node = node.right

# root = create_tree()
# nonrecursive_inorder_tree_walk(root)


# 不使用栈的非递归中序遍历,Morris方法
def nonrecursive_nonshed_inorder_tree_walk(root):
    node = root
    while node != None:
        # 如果当前节点的左孩子为空，则输出当前节点并将当前节点的右孩子作为“新的当前节点”。
        if not node.left:
            print node.val
            node = node.right
        # 如果当前节点的左孩子不为空，在当前节点的左子树中找到当前节点在中序遍历下的前驱节点。（前驱节点即“当前节点左子树的最右叶子节点”，此时最右节点的右儿子有两种情况，一种是指向当前节点，一种是为空）
        else:
            prev = node.left
            while prev.right is not None and prev.right != node:
                prev = prev.right
            # a) 如果前驱节点的右孩子为空，将它的右孩子设置为当前节点。当前节点更新为当前节点的左孩子。
            if prev.right == None:
                prev.right = node
                node = node.left
            # b) 如果前驱节点的右孩子为当前节点，将它的右孩子重新设为空（恢复树的形状）。输出当前节点。当前节点更新为当前节点的右孩子。
            else:
                prev.right = None
                print node.val
                node = node.right


root = create_tree()
nonrecursive_nonshed_inorder_tree_walk(root)