class C1(object):

    def leastOpsExpressTarget(self, a1, a2):
        """
        """
        v1, v2, v3 = (0, 0, 0)
        while a2:
            a2, v5 = divmod(a2, a1)
            if v3:
                v1, v2 = (min(v5 * v3 + v1, (v5 + 1) * v3 + v2), min((a1 - v5) * v3 + v1, (a1 - v5 - 1) * v3 + v2))
            else:
                v1, v2 = (v5 * 2, (a1 - v5) * 2)
            v3 += 1
        return min(v1, v3 + v2) - 1
