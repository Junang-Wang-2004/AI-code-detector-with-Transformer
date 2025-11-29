# Time:  O(n)
# Space: O(1)

class Solution(object):
    def maxDepthAfterSplit(self, seq):
        """
        """
        return [(i & 1) ^ (seq[i] == '(') for i, c in enumerate(seq)]


