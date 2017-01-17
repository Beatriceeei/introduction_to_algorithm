import random
def swp(A, i, j):
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp
def partition(A,p,r):
    pivot = A[p]
    step = p
    for i in xrange(p+1, r):
        if A[i] < pivot:
            step += 1
            swp(A, step, i)
    swp(A, step, p)
    return step


def randomized_partition(A, p, r):
    q = random.randint(p, r)
    swp(A, q, p)
    return partition(A, p, r)


def randomized_select(A, p, r, i):
    print p, r, i
    if p == r - 1:
        return A[p]
    q = randomized_partition(A, p, r)
    print A, q
    k = q - p + 1
    if k == i:
        return A[q]
    if k < i:
        return randomized_select(A, q+1, r, i - k)
    else:
        return randomized_select(A, p, q-1, i)

A = [32,17,22,8,10,4,5,84]
print randomized_select(A, 0, len(A), 7)