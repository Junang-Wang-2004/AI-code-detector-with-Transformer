class C1(object):

    def movesToMakeZigzag(self, a1):
        """
        """
        v1 = [0, 0]
        for v2 in range(len(a1)):
            v3 = a1[v2 - 1] if v2 - 1 >= 0 else float('inf')
            v4 = a1[v2 + 1] if v2 + 1 < len(a1) else float('inf')
            v1[v2 % 2] += max(a1[v2] - min(v3, v4) + 1, 0)
        return min(v1)
