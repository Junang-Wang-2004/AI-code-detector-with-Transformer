# Time:  O(nlogn)
# Space: O(1)
# greedy, sort
class Solution2(object):
    def maximumImportance(self, n, roads):
        """
        """
        degree = [0]*n
        for a, b in roads:
            degree[a] += 1
            degree[b] += 1
        degree.sort()
        return sum(i*x for i, x in enumerate(degree, 1))
