"""
Question - You are given two strings s and t.

String t is generated by random shuffling string s and then add one more letter at a random position.

Return the letter that was added to t.
"""

Solution -
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        t += s
        ans = ""
        for i in range(97,126):
            count = 0
            for j in range(0,len(t)):
                if t[j] == chr(i):
                    count += 1
            if count % 2 != 0:
                ans = chr(i)
                return ans
                break        
