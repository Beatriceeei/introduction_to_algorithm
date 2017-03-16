# -*- coding:utf8 -*-

from chapter12.tree_minimum import tree_minimum, tree_maximum
from chapter12 import prev_tree

def tree_successor(x):
    if x.right:
        return tree_minimum(x.right)
    y = x.prev
    while y and x == y.right:
        x = y
        y = y.prev
    return y

# head = prev_tree()
# print tree_successor(head.left.right.right).val


def tree_predecessor(x):
    if x.left:
        return tree_maximum(x.left)
    # 说明前去结点的做字数全部遍历完了
    y = x.prev
    while y and x == y.left:
        x = y
        y = y.prev
    return y

head = prev_tree()
print tree_predecessor(head.left).val