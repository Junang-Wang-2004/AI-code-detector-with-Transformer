class C1(object):

    def maxBoxesInWarehouse(self, a1, a2):
        """
        """
        a1.sort(reverse=True)
        v1 = 0
        for v2 in a1:
            if v2 > a2[v1]:
                continue
            v1 += 1
            if v1 == len(a2):
                break
        return v1
