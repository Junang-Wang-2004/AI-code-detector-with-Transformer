class C1(object):

    def largestNumber(self, a1, a2):
        """
        """
        v1 = [0]
        for v2 in range(1, a2 + 1):
            v1.append(-1)
            for v3, v4 in enumerate(a1):
                if v2 - v4 < 0:
                    continue
                v1[v2] = max(v1[v2], v1[v2 - v4] * 10 + v3 + 1)
        return str(max(v1[v2], 0))
