def hoare_partition(A, p, r):
    pivot = A[p]
    i, j = p, r
    while True:
        while A[j] > pivot:
            j -= 1
        while A[i] < pivot:
            i += 1
        if i < j:
            tmp = A[i]
            A[i] = A[j]
            A[j] = tmp
        else:
            return j

def quick_sort(A, p, r):
    if p<r:
        q = hoare_partition(A, p, r)
        quick_sort(A, p, q-1)
        quick_sort(A, q+1, r)

A = [5,4,3,2,1,6]
quick_sort(A, 0, 4)
print A