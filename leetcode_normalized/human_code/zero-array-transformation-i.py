class C1(object):

    def isZeroArray(self, a1, a2):
        """
        """
        v1 = [0] * (len(a1) + 1)
        for v2, v3 in a2:
            v1[v2] += 1
            v1[v3 + 1] -= 1
        v4 = 0
        for v5 in range(len(a1)):
            v4 += v1[v5]
            if a1[v5] > v4:
                return False
        return True
