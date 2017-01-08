class ListNode():
    def __init__(self, val):
        self.val = val
        self.next = None

def print_list(node):
    while True:
        print node.val,"->",
        if node.next == None:
            break
        node = node.next

def convert_array_to_list(A):
    node = ListNode(A[-1])
    for i in xrange(len(A)-2,-1,-1):
        new = ListNode(A[i])
        new.next = node
        node = new
    return node


def bucket_sort(A, k):
    buckets = [ListNode(0) for i in xrange(k)]
    for i in A:
        j = int(i*k)
        node = ListNode(i)
        iter,last = buckets[j],buckets[j]
        while iter and (iter.val < node.val):
            last = iter
            iter = last.next
        node.next = iter
        last.next = node
    return buckets


A = [0.78,0.17,0.39,0.26,0.72,0.94,0.21,0.12,0.23,0.68]
buckets = bucket_sort(A, 10)
for i, e in enumerate(buckets):
    print i, print_list(e)
