class Node():
    def __init__(self, x):
        self.value = x
        self.next = None

    def __str__(self):
        node = self
        s = ""
        while True:
            s += str(node.value) + "->"
            if node.next == None:
                break
            node = node.next
        return s

def array_to_list(A):
    n, end = None, None
    for i in xrange(len(A)-1,-1,-1):
        n = Node(A[i])
        n.next = end
        end = n
    return n

# def reverse_list(head):
#     if head == None or head.next == None:
#         return head
#     prev, curr, h = None, head, None
#     while curr:
#         h = curr
#         print "h",h
#         tmp = curr.next
#         print "tmp",tmp
#         curr.next = prev
#         print "curr.next",curr.next
#         prev = curr
#         print "prev",prev
#         curr = tmp
#         print "curr",curr
#     return h

def reverse_list(head):
    h, n, prev = Node(-1), head, None
    if head == None or head.next == None:
        return head
    while n:
        h.next = n
        n = n.next
        h.next.next = prev
        prev = h.next
    return h.next


a = array_to_list([1,2,3,4,5])
print reverse_list(a)