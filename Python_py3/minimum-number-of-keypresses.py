# Time:  O(n)
# Space: O(1)

import collections


# greedy, sort
class Solution(object):
    def minimumKeypresses(self, s):
        """
        """
        return sum(cnt*(i//9+1) for i, cnt in enumerate(sorted(iter(collections.Counter(s).values()), reverse=True)))
