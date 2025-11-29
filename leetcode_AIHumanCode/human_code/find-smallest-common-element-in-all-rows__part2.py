# Time:  O(m * n)
# Space: O(n)
import collections


class Solution2(object):
    def smallestCommonElement(self, mat):
        """
        """
        # assumed value is unique in each row
        counter = collections.Counter()
        for row in mat:
            for c in row:
                counter[c] += 1
                if counter[c] == len(mat):
                    return c
        return -1
