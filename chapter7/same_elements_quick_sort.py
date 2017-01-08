def swp(A, i, j):
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp
def same_partition(A, p, r):
    i, t, pivot = p-1, p-1, A[r]
    for j in xrange(p, r):
        if pivot > A[j]:
            i += 1
            t += 1
            swp(A, t, j)
            if i < t:
                swp(A, t, i)
        elif pivot == A[j]:
            t += 1
            swp(A, t, j)
    swp(A, t+1, r)
    return i+1,t+1



def quick_sort(A, p, r):
    if p < r:
        q, t = same_partition(A, p, r)
        quick_sort(A, p, q-1)
        quick_sort(A, t+1, r)

A = [2, 4, 1, 0, 7, 2, 9, 2]
print quick_sort(A, 0, 7)
print A