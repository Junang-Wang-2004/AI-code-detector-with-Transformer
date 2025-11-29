class C1(object):

    def maxValue(self, a1):
        """
        """
        v1 = [0] * len(a1)
        v1[0] = a1[0]
        for v2 in range(len(a1) - 1):
            v1[v2 + 1] = max(v1[v2], a1[v2 + 1])
        v3 = float('inf')
        for v2 in reversed(range(len(a1))):
            if v1[v2] > v3:
                v1[v2] = v1[v2 + 1]
            v3 = min(v3, a1[v2])
        return v1
