# -*- coding:utf8 -*-

def insert_sort(array):
    length = len(array)
    for i in xrange(1, length):
        tmp = array[i]
        j = i - 1
        while j > 0 and array[j] > tmp:
            array[j+1] = array[j]
            j -= 1 #退出循环前已经减1,当前指向比tmp小的最大元素
        array[j + 1] = tmp
    return array

array = [0, 1, 4, 3, 5, 2]
print insert_sort(array)