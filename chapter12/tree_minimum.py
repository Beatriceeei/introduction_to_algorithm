

from chapter12 import create_tree

def tree_minimum(x):
    while x.left:
        x = x.left
    return x

# head = create_tree()
# print tree_minimum(head).val

def tree_maximum(x):
    while x.right:
        x = x.right
    return x

# head = create_tree()
# print tree_maximum(head).val


def recursive_tree_minimum(x):
    if not x.left:
        return x
    else:
        return recursive_tree_minimum(x.left)

# head = create_tree()
# print recursive_tree_minimum(head).val

def recursive_tree_maximum(x):
    if not x.right:
        return x
    else:
        return recursive_tree_maximum(x.right)

# head = create_tree()
# print recursive_tree_maximum(head).val