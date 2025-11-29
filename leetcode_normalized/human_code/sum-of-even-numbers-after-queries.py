class C1(object):

    def sumEvenAfterQueries(self, a1, a2):
        """
        """
        v1 = sum((v for v2 in a1 if v2 % 2 == 0))
        v3 = []
        for v2, v4 in a2:
            if a1[v4] % 2 == 0:
                v1 -= a1[v4]
            a1[v4] += v2
            if a1[v4] % 2 == 0:
                v1 += a1[v4]
            v3.append(v1)
        return v3
