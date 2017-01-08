# -*- coding:utf8 -*-
import random
def permute_by_sorting(A):
    n = len(A)
    P = [0]*n
    for i in xrange(n):
        P[i] = random.randint(1, n**3)
    return [x[1] for x in sorted(enumerate(A),key=lambda x:P[x[0]])]

print permute_by_sorting([1,2,3,4,5])
