class C1(object):

    def minimumXORSum(self, a1, a2):
        """
        """
        v1 = [(float('inf'), float('inf'))] * 2 ** len(a2)
        v1[0] = (0, 0)
        for v2 in range(len(v1)):
            v3 = 1
            for v4 in range(len(a2)):
                if v2 & v3 == 0:
                    v1[v2 | v3] = min(v1[v2 | v3], (v1[v2][0] + (a1[v1[v2][1]] ^ a2[v4]), v1[v2][1] + 1))
                v3 <<= 1
        return v1[-1][0]
