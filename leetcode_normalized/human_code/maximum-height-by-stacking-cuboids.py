class C1(object):

    def maxHeight(self, a1):
        """
        """
        for v1 in a1:
            v1.sort()
        a1.append([0, 0, 0])
        a1.sort()
        v2 = [0] * len(a1)
        for v3 in range(1, len(a1)):
            for v4 in range(v3):
                if all((a1[v4][k] <= a1[v3][k] for v5 in range(3))):
                    v2[v3] = max(v2[v3], v2[v4] + a1[v3][2])
        return max(v2)
