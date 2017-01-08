# -*- coding:utf8 -*-

# method1: divide and conquer

def find_max_crossing_subarray(array, low, mid, high):
    left_num, left_sum, left_max_sum = low, 0, 0
    for k in xrange(mid, low-1, -1):
        left_sum += array[k]
        if left_sum > left_max_sum:
            left_max_sum = left_sum
            left_num = k
    right_num, right_sum, right_max_sum = high, 0, 0
    for k in xrange(mid+1, high+1):
        right_sum += array[k]
        if right_sum > right_max_sum:
            right_max_sum = right_sum
            right_num = k
    return left_num, right_num, left_max_sum+right_max_sum

# array = [1, -2, 1, 2, -2, 1]
# print find_max_crossing_subarray(array, 0, 2, 5)

def find_maximum_array(array, low, high):
    if low == high:
        return low, high, array[0]
    else:
        mid = (low + high) / 2
        left_low, left_high, left_sum = find_maximum_array(array, low, mid)
        right_low, right_high, right_sum = find_maximum_array(array, mid+1, high)
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(array, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum>= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum

# array = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
# print find_maximum_array(array, 0, 15)

# 暴力求解法4.1-2
def violence_find_maximum_array(array, low, high):
    sta, end = 0, 0
    max_sum, sum = 0, 0
    for i in xrange(low, high+1):
        sum = array[i]
        for j in xrange(i+1, high+1):
            sum += array[j]
            if sum > max_sum:
                max_sum = sum
                sta, end = i, j
    return sta, end, max_sum

# array = [13, -3, -25, 20, -3, -16, -23,18, 20, -7, 12, -5, -22, 15, -4, 7]
# print violence_find_maximum_array(array, 0, 15)

# non-recursive, linear
def linear_find_maximum_array(array, low, high):
    sta, end, max_sum, sum = 0, 0, -100000, 0
    for i in xrange(low, high+1):
        if sum >= 0:
            sum += array[i]
        else:
            sta, end, sum = i, i+1, array[i]
        if sum > max_sum:
            end, max_sum = i+1, sum
    return sta, end, max_sum

array = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
print linear_find_maximum_array(array, 0, 15)
array = [1, -5, 3, -4]
print linear_find_maximum_array(array,0, 3)
array = [-3,1]
print linear_find_maximum_array(array,0, 1)

def linear2(array, low, high):
    sta, end, max_benefit = 0, 0, 0
    for i in xrange(low, high+1):
        if array[i] < array[sta]:
            sta = i
        if array[i] - array[sta] > max_benefit:
            max_benefit = array[i] - array[sta]
    return max_benefit

array = [4, 1, 2, 1, 4]
print linear2(array,0,4)