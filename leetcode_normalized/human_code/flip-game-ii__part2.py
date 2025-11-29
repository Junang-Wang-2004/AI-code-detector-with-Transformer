class C1(object):

    def canWin(self, a1):
        """
        """
        v1 = {}

        def canWinHelper(a1):
            a1 = tuple(sorted((c for v2 in a1 if v2 >= 2)))
            if a1 not in v1:
                v1[a1] = any((not canWinHelper(a1[:i] + (j, v2 - 2 - j) + a1[i + 1:]) for v3, v2 in enumerate(a1) for v4 in range(v2 - 1)))
            return v1[a1]
        return canWinHelper(list(map(len, re.findall('\\+\\++', a1))))
