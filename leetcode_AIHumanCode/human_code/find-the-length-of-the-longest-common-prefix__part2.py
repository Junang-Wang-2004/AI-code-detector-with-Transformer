from functools import reduce
# Time:  O((n + m) * l)
# Space: O(n)
# hash table
class Solution2(object):
    def longestCommonPrefix(self, arr1, arr2):
        """
        """
        lookup = {0}
        for x in arr1:
            while x not in lookup:
                lookup.add(x)
                x //= 10
        result = 0
        for x in arr2:
            l = len(str(x))
            while x not in lookup:
                x //= 10
                l -= 1
            result = max(result, l)
        return result
