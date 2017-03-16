
from chapter12 import prev_tree,Node

def tree_insert(root, z):
    prev, curr = None, root
    while curr:
        prev = curr
        if curr.val > z.val:
            curr = curr.left
        else:
            curr = curr.right
    z.prev = prev
    if prev == None:
        root = z
    elif z.val < prev.val:
        prev.left = z
    else:
        prev.right = z
    return root

# root = prev_tree()
# print root.left.val
# root = tree_insert(root,Node(5))
# print root.left.left.right.val

def recursive_tree_insert(root,z):
    if not root.right and root.val < z.val:
        z.prev = root
        root.right = z
    elif not root.left and root.val > z.val:
        z.prev = root
        root.left = z
    elif root.val < z.val:
        recursive_tree_insert(root.right, z)
    else:
        recursive_tree_insert(root.left, z)
    return root

root = prev_tree()
print root.left.val
root = recursive_tree_insert(root,Node(5))
print root.left.left.right.right.val
