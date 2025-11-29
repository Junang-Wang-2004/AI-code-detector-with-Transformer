# Time:  O(n)
# Space: O(1)

class Solution(object):
    def isSubsequence(self, s, t):
        """
        """
        if not s:
            return True

        i = 0
        for c in t:
            if c == s[i]:
                i += 1
            if i == len(s):
                break
        return i == len(s)

