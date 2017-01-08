# -*- coding:utf8 -*-

# 5.1-2 由random(0,1)生成random(a,b)

from random import randint

def random_ab(a, b):
    interval = b-a+1
    i, s = 0, ''
    while 2**i < interval:
        s += str(randint(0, 1))
        i += 1
    random_num = int(s, 2)
    if random_num < interval:
        return random_num+a
    else:
        return random_ab(a, b)
# a, b = 1, 7
# A = [0 for i in xrange(a, b+1)]
# for i in xrange(100000):
#     A[random_ab(a, b)-a] += 1
# print A
# print map(lambda e:e/100000.0, A)

# 由random(1,7)生成random(1,10)
def random10():
    first, second = random_ab(1, 7),random_ab(1, 7)
    if (first-1)*7+second-1 < 40:
        return (first*7+second-1)%10
    return random10()

# a, b = 1, 10
# A = [0 for i in xrange(a, b+1)]
# for i in xrange(100000):
#     A[random10()] += 1
# print A
# print map(lambda e:e/100000.0, A)
#

# 5.1-3 偏执随机数生成非偏结果
def random_p(p):
    if randint(1, 10)<=p*10:
        return 0
    else:
        return 1

def biased_random(p):
    n1, n2 = random_p(p), random_p(p)
    if n1 != n2:
        return n1
    else:
        return biased_random(p)

A = [0,0]
for i in xrange(100000):
    A[biased_random(0.3)] += 1
print A