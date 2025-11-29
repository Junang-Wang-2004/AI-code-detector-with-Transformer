from functools import reduce
# Time:  O(blogb)
# Space: O(logb)
# brute force, hash table
class Solution4(object):
    def numberCount(self, a, b):
        """
        """
        return sum(len(set(str(x))) == len(str(x)) for x in range(a, b+1))
