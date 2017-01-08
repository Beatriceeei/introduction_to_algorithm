# -*- coding:utf8 -*-
# 2.2
def bubble_sort(array):
    length = len(array)
    for i in xrange(length):
        for j in xrange(length-1,i-1,-1):
            if array[j] <  array[j-1]:
                tmp = array[j]
                array[j] = array[j-1]
                array[j-1] = tmp
    return array

array = [7,6,5,4,3,2,1]
print bubble_sort(array)