import itertools

class C1(object):

    def maximumCostSubstring(self, a1, a2, a3):
        """
        """

        def kadane(a1):
            v1 = v2 = 0
            for v3 in a1:
                v2 = max(v2 + (lookup[v3] if v3 in lookup else ord(v3) - ord('a') + 1), 0)
                v1 = max(v1, v2)
            return v1
        v1 = {}
        for v2, v3 in zip(a2, a3):
            v1[v2] = v3
        return kadane(a1)
