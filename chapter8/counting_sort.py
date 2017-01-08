def counting_sort(A, B, k):
    C = [0] * k
    length = len(A)
    for j in xrange(length):
        C[A[j]] += 1
    for i in xrange(1,k):
        C[i] = C[i] + C[i-1]
    for j in xrange(length-1,-1,-1):
        B[C[A[j]]-1] = A[j]
        C[A[j]] -= 1

A = [6,0,2,0,1,3,4,6,1,3,2]
B = [0] * len(A)
k = max(A) + 1
counting_sort(A, B, k)
print B