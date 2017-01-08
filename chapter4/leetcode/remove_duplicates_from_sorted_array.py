# 26. Remove Duplicates from Sorted Array
# Do not allocate extra space for another array, you must do this in place with constant memory.
#
# For example,
# Given input array nums = [1,1,2],
#
# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.

def remove_duplicates(nums):
    length = len(nums)
    cnt, last = 0, None
    for i in xrange(length):
        if nums[i]!=last:
            cnt += 1
        else:
            pass
        last = nums[i]
    return cnt

nums = [1,1,2]
print remove_duplicates(nums)