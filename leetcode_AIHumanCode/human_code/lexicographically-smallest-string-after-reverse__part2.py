# Time:  O(n^2)
# Space: O(n)
# brute force
class Solution2(object):
    def lexSmallest(self, s):
        """
        """
        result = s
        for k in range(2, len(s)+1):
            result = min(result, s[:k][::-1]+s[k:], s[:-k]+s[-k:][::-1])
        return result


