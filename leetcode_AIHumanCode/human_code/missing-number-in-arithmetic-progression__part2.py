# Time:  O(n)
# Space: O(1)
class Solution2(object):
    def missingNumber(self, arr):
        """
        """
        return (min(arr)+max(arr))*(len(arr)+1)//2 - sum(arr)
