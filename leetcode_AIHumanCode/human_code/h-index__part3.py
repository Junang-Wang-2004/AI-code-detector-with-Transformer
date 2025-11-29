# Time:  O(nlogn)
# Space: O(n)
class Solution3(object):
    def hIndex(self, citations):
        """
        """
        return sum(x >= i + 1 for i, x in enumerate(sorted(citations, reverse=True)))


