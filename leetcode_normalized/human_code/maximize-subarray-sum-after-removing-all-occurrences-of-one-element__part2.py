import collections

class C1(object):

    def maxSubarraySum(self, a1):
        """
        """
        v1 = float('-inf')
        v2 = v3 = v4 = 0
        v5 = collections.defaultdict(int)
        for v6 in a1:
            v2 += v6
            v1 = max(v1, v2 - v3)
            if v6 < 0:
                v5[v6] = min(v5[v6], v4) + v6
                v3 = min(v3, v5[v6])
            v4 = min(v4, v2)
            v3 = min(v3, v4)
        return v1
