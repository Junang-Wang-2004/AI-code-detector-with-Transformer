class Solution(object):
    def findTheDifference(self, s, t):
        return chr(sum(ord(ch) for ch in t) - sum(ord(ch) for ch in s))
