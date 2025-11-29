class C1(object):

    def sumImbalanceNumbers(self, a1):
        """
        """
        v1 = 0
        for v2 in range(len(a1)):
            v3 = {a1[v2]}
            v4 = 0
            for v5 in reversed(range(v2)):
                if a1[v5] not in v3:
                    v3.add(a1[v5])
                    v4 += 1 - (a1[v5] - 1 in v3) - (a1[v5] + 1 in v3)
                v1 += v4
        return v1
