class Node():
    def __init__(self, x, left=None, right=None, prev=None):
        self.val = x
        self.left = left
        self.right = right
        self.prev = prev

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

def prev_tree():
    node1 = Node(2)
    node2 = Node(4)
    node3 = Node(3, node1, node2)
    node1.prev, node2.prev = node3, node3
    node4 = Node(9)
    node5 = Node(13,node4)
    node4.prev = node5
    node6 = Node(7, None, node5)
    node5.prev = node6
    node7 = Node(6, node3, node6)
    node3.prev, node6.prev = node7, node7
    node9 = Node(17)
    node10 = Node(20)
    node11 = Node(18, node9, node10)
    node9.prev,node10.prev = node11, node11
    node8 = Node(15, node7, node11)
    node7.prev, node11.prev = node8,node8
    return node8

