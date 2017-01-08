def swp(A, i, j):
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp
def partition(A, p, r):
    pivot, i = A[r], p - 1
    for j in xrange(p, r):
        if A[j] <= pivot:
            i += 1
            swp(A, i, j)
    swp(A, i+1, r)
    return i+1


def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q-1)
        quick_sort(A, q+1, r)

A = [1,1,1,1]
print partition(A, 0, 3)
# quick_sort(A, 0, 4)
# print A