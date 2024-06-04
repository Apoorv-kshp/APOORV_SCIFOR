"""
Question - There is a function signFunc(x) that returns:

    1 if x is positive.
    -1 if x is negative.
    0 if x is equal to 0.

You are given an integer array nums. Let product be the product of all values in the array nums.

Return signFunc(product).
"""

Solution - 
class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums[0] > 0:
            a = 1
        elif nums[0] < 0:
            a = -1
        else:
            return 0
        for i in range(1,len(nums)):
            b = nums[i] * a
            if b > 0:
                a = 1
            elif b < 0:
                a = -1
            else:
                a = 0
                break
        return a
