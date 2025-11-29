# Time:  O(n)
# Space: O(n)
# graph, hash table
class Solution2(object):
    def findChampion(self, n, edges):
        """
        """
        lookup = {v for _, v in edges}
        return next(u for u in range(n) if u not in lookup) if len(lookup) == n-1 else -1
