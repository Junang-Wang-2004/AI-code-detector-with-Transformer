class C1(object):

    def makeArrayPositive(self, a1):
        """
        """
        v1 = 10 ** 18
        v2 = 0
        v3 = a1[0] + a1[1]
        v4 = a1[0]
        v5 = 0
        for v6 in range(2, len(a1)):
            v7 = v3 + a1[v6]
            if v7 - v5 <= 0:
                v7 = v3 + v1
                v2 += 1
            v5 = max(v5, v4)
            v3, v4 = (v7, v3)
        return v2
