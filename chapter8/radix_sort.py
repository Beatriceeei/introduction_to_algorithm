# 8.3-1
def counting_sort(A, B, k, j):
    C = [0]*k
    length = len(A)
    for i in xrange(length):
        C[A[i][j]] += 1
    for i in xrange(1,k):
        C[i] += C[i-1]
    for i in xrange(length-1,-1,-1):
        B[C[A[i][j]]-1] = A[i]
        C[A[i][j]] -= 1
    return B


def convert_char_to_num(X):
    X = [[ord(i)-ord('A') for i in x] for x in X]
    return X

def convert_num_to_char(X):
    X = [''.join([chr(i+ord('A')) for i in x]) for x in X]
    return X


def radix_sort(X, d):
    for i in xrange(d-1,-1,-1):
        Y = [[] for k in X]
        X = counting_sort(X, Y, ord('Z'), i)
    return X

X = ['COW','DOG','SEA','RUG','ROW','BOX','MOB']
X = convert_char_to_num(X)
X = radix_sort(X,3)
X = convert_num_to_char(X)
print X

