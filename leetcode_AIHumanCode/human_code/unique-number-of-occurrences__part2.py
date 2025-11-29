# Time:  O(n)
# Space: O(n)
class Solution2(object):
    def uniqueOccurrences(self, arr):
        """
        """
        count = collections.Counter(arr)
        return len(count) == len(set(count.values()))
