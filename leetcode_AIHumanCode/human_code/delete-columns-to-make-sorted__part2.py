# Time:  O(n * l)
# Space: O(n)
import itertools


class Solution2(object):
    def minDeletionSize(self, A):
        """
        """
        result = 0
        for col in zip(*A):
            if any(col[i] > col[i+1] for i in range(len(col)-1)):
                result += 1
        return result
