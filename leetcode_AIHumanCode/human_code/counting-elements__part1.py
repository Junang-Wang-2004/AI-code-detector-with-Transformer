# Time:  O(n)
# Space: O(n)

class Solution(object):
    def countElements(self, arr):
        """
        """
        lookup = set(arr)
        return sum(1 for x in arr if x+1 in lookup)


