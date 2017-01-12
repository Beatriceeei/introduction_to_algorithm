def mininum(A):
    min = None
    for i in xrange(len(A)):
        if min == None or A[i] < min:
            min = A[i]
    return min

A = [5,4,3,2,1]
print mininum(A)