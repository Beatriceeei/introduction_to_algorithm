# -*- coding:utf8 -*-

# 53. Maximum Subarray
# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
#
# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.

def maximum_subarray(nums):
    sum, max_sum = 0, -100000
    length = len(nums)
    for i in xrange(length):
        if sum < 0:
            sum = nums[i]
        else:
            sum += nums[i]
        if sum > max_sum:
            max_sum = sum
    return max_sum

nums = [-1]
print maximum_subarray(nums)

# 152. Maximum Product Subarray
# Find the contiguous subarray within an array (containing at least one number) which has the largest product.
#
# For example, given the array [2,3,-2,4],
# the contiguous subarray [2,3] has the largest product = 6.

def maximum_product_subarray(nums):
    prev_max_product,prev_min_product, max_product, min_product, result = nums[0], nums[0], nums[0],nums[0], nums[0]
    length = len(nums)
    for i in xrange(1, length):
        max_product = max(prev_max_product*nums[i], prev_min_product*nums[i], nums[i])
        min_product = min(prev_min_product*nums[i], prev_max_product*nums[i], nums[i])
        result = max(result, max_product, min_product)
        prev_max_product = max_product
        prev_min_product = min_product
    return result

nums = [-2, -3, -4]
print maximum_product_subarray(nums)

# 209. Minimum Size Subarray Sum
# Given an array of n positive integers and a positive integer s, find the minimal length of a subarray of which the sum ≥ s. If there isn't one, return 0 instead.
#
# For example, given the array [2,3,1,2,4,3] and s = 7,
# the subarray [4,3] has the minimal length under the problem constraint.

def minimum_size_subarray(s, nums):
    length, sta, min_cnt, sum = len(nums), 0, len(nums)+1, 0
    for i in xrange(length):
        sum += nums[i]
        while sum >= s:
            min_cnt = min(min_cnt, i-sta+1)
            sum -= nums[sta]
            sta += 1
    return min_cnt if min_cnt!=length+1 else 0

array = [1,2,3,4,5]
print minimum_size_subarray(11,array)
array = [2,3,1,2,4,3]
print minimum_size_subarray(7,array)
array = [1,1]
print minimum_size_subarray(3, array)