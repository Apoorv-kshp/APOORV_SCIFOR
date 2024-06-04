"""
Question :-
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""

Solution -

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count = 0
        for i in nums:
            if i == 0:
                count += 1
        for i in range(0,count):
            nums.remove(0)
        for i in range(0,count):
            nums.append(0)
