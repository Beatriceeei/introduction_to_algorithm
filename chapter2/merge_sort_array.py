# -*- coding:utf8 -*-

# 88. Merge Sorted Array
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
#
# Note:
# You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        tmp = nums1[:m]
        i, j = 0, 0
        for k in xrange(0, m+n):
            if i>=m:
                nums1[k:] = nums2[j:]
                break
            elif j>=n:
                nums1[k:] = tmp[i:]
                break
            elif tmp[i] > nums2[j]:
                nums1[k] = nums2[j]
                j += 1
            else:
                nums1[k] = tmp[i]
                i += 1

nums1 = [2,0]
nums2 = [1]
Solution().merge(nums1, 1, nums2, 1)