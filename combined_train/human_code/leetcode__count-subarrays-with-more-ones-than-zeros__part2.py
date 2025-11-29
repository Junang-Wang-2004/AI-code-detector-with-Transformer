class C1(object):

    def subarraysWithMoreZerosThanOnes(self, a1):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = {0: -1}
        v3 = [0] * len(a1)
        v4 = v5 = 0
        for v6, v7 in enumerate(a1):
            v5 += 1 if v7 == 1 else -1
            if v5 not in v2:
                if v5 > 0:
                    v3[v6] = v6 + 1
            else:
                v8 = v2[v5]
                if v8 != -1:
                    v3[v6] = v3[v8]
                if v7 > 0:
                    v3[v6] += v6 - 1 - v8
            v2[v5] = v6
            v4 = (v4 + v3[v6]) % v1
        return v4
