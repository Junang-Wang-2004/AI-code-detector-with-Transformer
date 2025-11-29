class C1(object):

    def maxPower(self, a1):
        """
        """
        v1, v2 = (1, 1)
        for v3 in range(1, len(a1)):
            if a1[v3] == a1[v3 - 1]:
                v2 += 1
            else:
                v2 = 1
            v1 = max(v1, v2)
        return v1
