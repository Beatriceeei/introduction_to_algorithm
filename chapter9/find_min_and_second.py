class Node():
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

def build_tree(A, i, j):
    if j-i == 0:
        return Node(A[i], None, None)
    left = build_tree(A, i, (j+i)/2)
    right = build_tree(A, (j+i)/2+1, j)
    node = Node(min(left.value,right.value),left, right)
    return node

def findsecond(head,minimum):
    node = head
    if not node.left and not node.right:
        return node.value if node.value!=minimum else float("inf")
    if node.left and node.right:
        if node.left.value == node.value:
            return min(node.right.value, findsecond(node.left,minimum))
        else:
            return min(node.left.value, findsecond(node.right,minimum))
    else:
        value = node.left.value or node.right.value
        return value if value!=minimum else float("inf")

A = [95,41,33,2,31,30,294,23]
node = build_tree(A,0,7)
print node.value
print findsecond(node,node.value)