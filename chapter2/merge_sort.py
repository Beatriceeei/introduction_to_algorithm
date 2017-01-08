# -*- coding:utf8 -*-

def merge(array, p, q, r):
    left = array[p:q+1]
    left.append(-1)
    right = array[q+1:r+1]
    right.append(-1)
    i, j = 0, 0
    for k in xrange(p, r+1):
        if left[i] == -1:
            array[k] = right[j]
        elif right[j] == -1:
            array[k] = left[i]
        elif left[i] > right[j]:
            array[k] = right[j]
            j += 1
        elif left[i] <= right[j]:
            array[k] = left[i]
            i += 1
    return array

# 2.3.2 不使用哨兵,一个数组被复制回array后立刻停止,将另一数组接上
def merge2(array, p, q, r):
    left = array[p:q+1]
    right = array[q+1:r+1]
    i, j = 0, 0
    for k in xrange(p, r+1):
        if i >= q - p + 1:
            array[k:r+1] = right[j:]
            break
        elif j >= r - q:
            array[k:r+1] = left[i:]
            break
        elif left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
    return array

array = [1,3,5,7,2]
print merge2(array, 0, 3, 4)


def merge_sort(array, p, r):
    if p < r:
        mid = (p + r)/2
        merge_sort(array, p, mid)
        merge_sort(array, mid+1, r)
        merge2(array, p, mid, r)
    return array

# array = [2,1,5,7,2,4,6,8]
# print merge(array, 0, 0, 1)

# array = [3,41,52,26,38,57,9,49]
# print merge_sort(array,0,7)

