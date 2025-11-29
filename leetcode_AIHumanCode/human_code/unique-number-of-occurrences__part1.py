# Time:  O(n)
# Space: O(n)

import collections


class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        """
        count = collections.Counter(arr)
        lookup = set()
        for v in count.values():
            if v in lookup:
                return False
            lookup.add(v)
        return True


