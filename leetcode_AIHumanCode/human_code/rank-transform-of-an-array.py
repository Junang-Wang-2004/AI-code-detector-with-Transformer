# Time:  O(nlogn)
# Space: O(n)

class Solution(object):
    def arrayRankTransform(self, arr):
        """
        """
        return list(map({x: i+1 for i, x in enumerate(sorted(set(arr)))}.get, arr))
