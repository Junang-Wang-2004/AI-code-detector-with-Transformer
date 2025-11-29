class C1(object):

    def beautifulPartitions(self, a1, a2, a3):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = {'2', '3', '5', '7'}
        v3 = [0] * len(a1)
        for v4 in range(a3 - 1, len(a1)):
            if a1[0] in v2 and a1[v4] not in v2:
                v3[v4] = 1
        for v5 in range(2, a2 + 1):
            v6 = [0] * len(a1)
            v7 = int(v5 == 1)
            for v4 in range(v5 * a3 - 1, len(a1)):
                if a1[v4 - a3 + 1] in v2:
                    v7 = (v7 + v3[v4 - a3]) % v1
                if a1[v4] not in v2:
                    v6[v4] = v7
            v3 = v6
        return v3[-1]
