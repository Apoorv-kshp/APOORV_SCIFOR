"""
Question :-
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
"""

Solution - 

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        ans = 0
        for i in digits:
            ans = (10 * ans) + i
        ans += 1
        l = []
        while ans != 0:
            l.insert(0,(ans % 10))
            ans /= 10
        return l
