# Time:  O(n * k)
# Space: O(k)
class Solution2(object):
    def strStr(self, haystack, needle):
        """
        """
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i : i + len(needle)] == needle:
                return i
        return -1


