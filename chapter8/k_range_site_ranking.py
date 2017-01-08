# 8-2.e
def swp(A, i, j):
    k = A[i]
    A[i] = A[j]
    A[j] = k
def k_range_site_ranking(A, k):
    count = [0] * k
    length = len(A)
    for i in xrange(length):
        count[A[i]-1] += 1
    for i in xrange(1,k):
        count[i] += count[i-1]
    for i in xrange(length-1,-1,-1):
        swp(A, i, count[A[i]-1]-1)
        count[A[i]-1] -= 1

A = [5,4,3,2,1]
k_range_site_ranking(A,5)
print A