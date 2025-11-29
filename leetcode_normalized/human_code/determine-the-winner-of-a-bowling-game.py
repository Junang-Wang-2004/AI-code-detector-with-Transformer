class C1(object):

    def isWinner(self, a1, a2):
        """
        """
        v1 = 2

        def f(a1):
            v1 = v2 = 0
            for v3 in range(len(a1)):
                v1 += 2 * a1[v3] if v2 else a1[v3]
                v2 += a1[v3] == 10
                if v3 - v1 >= 0:
                    v2 -= a1[v3 - v1] == 10
            return v1
        v2, v3 = (f(a1), f(a2))
        return 1 if v2 > v3 else 2 if v2 < v3 else 0
