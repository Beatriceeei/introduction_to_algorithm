# -*- coding:utf8 -*-


# 398. Random Pick Index
# Given an array of integers with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.
#
# Note:
# The array size can be very large. Solution that uses too much extra space will not pass the judge.
import random
class Solution(object):

    def __init__(self, nums):
        """

        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums
        self.numsSize = len(nums)

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        result, count = -1, 0
        for i in xrange(self.numsSize):
            if self.nums[i] != target:
                continue
            if random.randint(0, count) == 0:
                result = i
            count += 1
        return result


nums = [1,2,1,1,1]
print Solution(nums).pick(1)


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)