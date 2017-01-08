# -*- coding:utf8 -*-

def merge(array, p, q, r):
    left = array[p:q+1]
    right = array[q+1:r+1]
    left.append(-1)
    right.append(-1)
    i, j = 0, 0
    cnt = 0
    for k in xrange(p, r+1):
        if right[j] == -1:
            array[k] = left[i]
            i+=1
        elif left[i] == -1:
            array[k] = right[j]
            j += 1
        elif left[i] > right[j]:
            cnt += q+j+1-k # 关注小数往前排的情况,往前排多少就有多少逆序对
            array[k] = right[j]
            j += 1
        else:
            array[k] = left[i]
            i += 1
    return cnt

# array = [2,4,6,8,1,3,5,7]
# print merge(array,0,3,7)

def merge_sort(array, p, r):
    cnt = 0
    if p < r:
        mid = (p + r)/2
        merge_sort(array, p, mid)
        merge_sort(array, mid+1, r)
        cnt+=merge(array, p, mid, r)
    return array, cnt


array = [2,4,6,8,1,3,5,7]
print merge_sort(array,0,7)

