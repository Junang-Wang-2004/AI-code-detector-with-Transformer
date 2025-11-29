# Time:  O(n^2)
# Space: O(n)
# brute force
class Solution3(object):
    def lexSmallest(self, s):
        """
        """
        return min(min(s[:k][::-1]+s[k:], s[:-k]+s[-k:][::-1]) for k in range(1, len(s)+1))
