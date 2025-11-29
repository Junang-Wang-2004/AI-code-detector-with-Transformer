# Time:  O(m * n)
# Space: O(k)
import collections


class Solution2(object):
    def kWeakestRows(self, mat, k):
        """
        """
        lookup = collections.OrderedDict()
        for j in range(len(mat[0])):
            for i in range(len(mat)):
                if mat[i][j] or i in lookup:
                    continue
                lookup[i] = True
                if len(lookup) == k:
                    return list(lookup.keys())
        for i in range(len(mat)):
            if i in lookup:
                continue
            lookup[i] = True
            if len(lookup) == k:
                break
        return list(lookup.keys())


