import sortedcontainers

class C1(object):

    def maxDepthBST(self, a1):
        """
        """
        v1 = sortedcontainers.SortedDict({float('-inf'): 0, float('inf'): 0})
        v2 = list(v1.values())
        v3 = 0
        for v4 in a1:
            v5 = v1.bisect_right(v4)
            v1[v4] = max(v2[v5 - 1:v5 + 1]) + 1
            v3 = max(v3, v1[v4])
        return v3
