"""
Question:-
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        for i in range(97,126):
            c = chr(i)
            a = s.count(c)
            b = t.count(c)
            if a != b :
                return False
                break
        return True
