class Solution:
    def isSubsequence(self, s, t):
        ptr = 0
        for ch in s:
            ptr = t.find(ch, ptr)
            if ptr == -1:
                return False
            ptr += 1
        return True
