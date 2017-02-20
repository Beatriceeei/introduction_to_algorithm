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

def recursive_postorder_tree_walk(node):
    if node:
        recursive_postorder_tree_walk(node.left)
        recursive_postorder_tree_walk(node.right)
        print node.val


# root = create_tree()
# recursive_postorder_tree_walk(root)

def nonrecursive_postorder_tree_walk(root):
    shed = [root]
    pre = None
    while shed:
        node = shed[-1]
        print "node:",node.val,"shed:",[e.val for e in shed]
        if (not node.left and not node.right) or (pre and (pre==node.left or pre==node.right)):
            print node.val
            shed.pop(-1)
            pre = node
        else:
            if node.right:
                shed.append(node.right)
            if node.left:
                shed.append(node.left)


root = create_tree()
nonrecursive_postorder_tree_walk(root)

def nonrecursive_noshed_postorder_tree_walk(root):
    pass