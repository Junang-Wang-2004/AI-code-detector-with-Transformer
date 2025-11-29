# Time:  O(26)
# Space: O(26)
import collections


# freq table, greedy
class Solution2(object):
    def minimumPushes(self, word):
        """
        """
        return sum(x*(i//(9-2+1)+1) for i, x in enumerate(sorted(iter(collections.Counter(word).values()), reverse=True)))
