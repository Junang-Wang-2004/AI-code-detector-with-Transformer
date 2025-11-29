class C1(object):

    def maximumRequests(self, a1, a2):
        """
        """

        def evaluate(a1, a2, a3):
            v1 = [0] * a1
            v2, v3 = (1, 0)
            for v4 in range(len(a2)):
                if v2 & a3:
                    v1[a2[v4][0]] -= 1
                    v1[a2[v4][1]] += 1
                    v3 += 1
                v2 <<= 1
            return v3 if all((c == 0 for v5 in v1)) else 0
        return max((evaluate(a1, a2, i) for v1 in range(1 << len(a2))))
