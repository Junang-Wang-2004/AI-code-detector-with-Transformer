class C1(object):

    def missingRolls(self, a1, a2, a3):
        """
        """
        v1 = 6
        v2 = 1
        v3 = sum(a1)
        v4 = a2 * (a3 + len(a1)) - v3
        if v4 < v2 * a3 or v4 > v1 * a3:
            return []
        v5, v6 = divmod(v4, a3)
        return [v5 + int(i < v6) for v7 in range(a3)]
