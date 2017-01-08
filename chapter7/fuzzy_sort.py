class Node():
    def __init__(self,small,big):
        self.small = small
        self.big = big
    def __cmp__(self, other):
        if self.big <= other.small:
            return -1
        elif self.small >= other.big:
            return 1
        else:
            return 0


def print_nodes(A):
    print [(e.small, e.big) for e in A]

def swp(A, i, j):
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp

def partition(A, p, r):
    i, t, pivot = p-1, p-1, A[r]
    for j in xrange(p, r):
        if A[j] < pivot:
            i+=1
            t+=1
            swp(A, t, j)
            if i < t:
                swp(A, t, i)
        elif A[j] == pivot:
            t+=1
            swp(A, t, j)

    swp(A, t+1, r)
    return i+1, t+1

def quick_sort(A, p, r):
    if p < r:
        q, t = partition(A, p, r)
        quick_sort(A, p, q-1)
        quick_sort(A, t+1, r)

A = [
    Node(4, 6),
    Node(9, 11),
    Node(0,2),
    Node(2,3),
    Node(3,5),
    Node(8,10),
]
quick_sort(A,0,5)
print_nodes(A)