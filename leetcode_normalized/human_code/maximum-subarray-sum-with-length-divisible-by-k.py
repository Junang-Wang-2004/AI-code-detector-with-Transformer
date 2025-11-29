class C1(object):

    def maxSubarraySum(self, a1, a2):
        """
        """
        v1 = [float('inf')] * a2
        v1[-1] = 0
        v2 = 0
        v3 = float('-inf')
        for v4, v5 in enumerate(a1):
            v2 += v5
            v3 = max(v3, v2 - v1[v4 % a2])
            v1[v4 % a2] = min(v1[v4 % a2], v2)
        return v3
