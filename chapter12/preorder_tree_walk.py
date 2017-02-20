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

def recursive_preorder_tree_walk(node):
    if node:
        print node.val
        recursive_preorder_tree_walk(node.left)
        recursive_preorder_tree_walk(node.right)

# root = create_tree()
# recursive_preorder_tree_walk(root)

def nonrecursive_preorder_tree_walk(root):
    shed = []
    node = root
    while node or shed:
        print node.val,shed
        f=False
        while node.left:
            if node.right:
                shed.append(node.right)
            node = node.left
            f=True
            break
        if f:
            continue
        if shed:
            node = shed.pop(-1)
        else:
            node = node.right


def nonrecursive(root):
    shed = [root]
    while shed:
        node = shed.pop(-1)
        print node.val
        if node.right:
            shed.append(node.right)
        if node.left:
            shed.append(node.left)


# root = create_tree()
# nonrecursive_preorder_tree_walk(root)

# root = create_tree()
# nonrecursive(root)

def nonrecursive_nonshed_preorder_tree_walk(root):
    node = root
    while node:
        if node.left==None:
            print node.val
            node = node.right
        else:
            prev = node.left
            while prev.right and prev.right!=node:
                prev = prev.right
            if prev.right==None:
                prev.right = node
                print node.val
                node = node.left
            else:
                prev.right = None
                node = node.right

root = create_tree()
nonrecursive_nonshed_preorder_tree_walk(root)

