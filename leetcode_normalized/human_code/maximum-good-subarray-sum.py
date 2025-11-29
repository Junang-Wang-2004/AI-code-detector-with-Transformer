import collections

class C1(object):

    def maximumSubarraySum(self, a1, a2):
        """
        """
        v1 = collections.defaultdict(lambda: float('inf'))
        v2 = 0
        v3 = float('-inf')
        for v4 in a1:
            v1[v4] = min(v1[v4], v2)
            v2 += v4
            v3 = max(v3, v2 - v1[v4 - a2], v2 - v1[v4 + a2])
        return v3 if v3 != float('-inf') else 0
