class C1(object):

    def maximumGain(self, a1, a2, a3):
        """
        """

        def score(a1, a2, a3):
            v1 = v2 = 0
            for v3 in range(len(a1)):
                a1[v1] = a1[v3]
                v1 += 1
                if v1 >= 2 and a1[v1 - 2:v1] == a2:
                    v1 -= 2
                    v2 += a3
            a1[:] = a1[:v1]
            return v2
        a1, v2, v3 = (list(a1), list('ab'), list('ba'))
        if a2 < a3:
            a2, a3 = (a3, a2)
            v2, v3 = (v3, v2)
        return score(a1, v2, a2) + score(a1, v3, a3)
