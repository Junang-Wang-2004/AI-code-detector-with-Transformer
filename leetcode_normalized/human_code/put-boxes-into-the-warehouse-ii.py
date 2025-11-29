class C1(object):

    def maxBoxesInWarehouse(self, a1, a2):
        """
        """
        a1.sort(reverse=True)
        v1, v2 = (0, len(a2) - 1)
        for v3 in a1:
            if v3 <= a2[v1]:
                v1 += 1
            elif v3 <= a2[v2]:
                v2 -= 1
            if v1 > v2:
                break
        return v1 + (len(a2) - 1 - v2)
