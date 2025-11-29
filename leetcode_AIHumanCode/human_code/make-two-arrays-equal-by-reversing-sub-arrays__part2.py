# Time:  O(nlogn)
# Space: O(1)
class Solution2(object):
    def canBeEqual(self, target, arr):
        """
        """
        target.sort(), arr.sort()
        return target == arr
