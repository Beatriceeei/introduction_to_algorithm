
from chapter12 import prev_tree, Node
from chapter12.tree_successor import tree_successor

def trans_parent(root, old, new):
    if old.prev == None:
        root = new
    elif old == old.prev.left:
        old.prev.left = new
    else:
        old.prev.right = new
    if new:
        new.prev = old.prev
    return root

def tree_delete(root, z):
    if not z.left and not z.right:
        root = trans_parent(root, z, None)
    elif not z.right:
        root = trans_parent(root, z, z.left)
    elif not z.left:
        root = trans_parent(root, z, z.right)
    else:
        successor = tree_successor(z)
        if not successor == z.right:
            root = trans_parent(root, successor, successor.right)
            successor.right = z.right
            z.right.prev = successor
        root = trans_parent(root, z, successor)
        successor.left = z.left
        z.left.prev = z
    return root

root = prev_tree()
root = tree_delete(root,root)
print root.right.val