class C1(object):

    def maxBoxesInWarehouse(self, a1, a2):
        """
        """
        a1.sort()
        for v1 in range(1, len(a2)):
            a2[v1] = min(a2[v1], a2[v1 - 1])
        v2, v3 = (0, 0)
        for v4 in reversed(a2):
            if a1[v3] > v4:
                continue
            v2 += 1
            v3 += 1
            if v3 == len(a1):
                break
        return v2
