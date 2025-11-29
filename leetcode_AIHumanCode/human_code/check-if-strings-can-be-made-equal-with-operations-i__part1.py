# Time:  O(1)
# Space: O(1)

import collections


# freq table
class Solution(object):
    def canBeEqual(self, s1, s2):
        """
        """
        return all(collections.Counter(s1[j] for j in range(i, len(s1), 2)) == collections.Counter(s2[j] for j in range(i, len(s2), 2)) for i in range(2))


