class C1(object):

    def longestSubarray(self, a1):
        """
        """
        v1 = [1] * len(a1)
        for v2 in range(len(a1) - 1):
            if a1[v2] <= a1[v2 + 1]:
                v1[v2 + 1] = v1[v2] + 1
        v3 = [1] * len(a1)
        for v2 in reversed(range(len(a1) - 1)):
            if a1[v2] <= a1[v2 + 1]:
                v3[v2] = v3[v2 + 1] + 1
        v4 = min(max(v1) + 1, len(a1))
        for v2 in range(1, len(a1) - 1):
            if a1[v2 - 1] <= a1[v2 + 1]:
                v4 = max(v4, v1[v2 - 1] + 1 + v3[v2 + 1])
        return v4
