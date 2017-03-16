


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

def tree_search(x, k):
    print x.val
    if x == None or x.val == k:
        return x
    if x.val < k:
        return tree_search(x.right, k)
    else:
        return tree_search(x.left, k)

# head = create_tree()
# print tree_search(head, 6).val

def iterative_tree_search(x, k):
    node = x
    while node and k!=node.val:
        print node.val
        if k < node.val:
            node = node.left
        else:
            node = node.right
    return node

head = create_tree()
print iterative_tree_search(head, 6).val