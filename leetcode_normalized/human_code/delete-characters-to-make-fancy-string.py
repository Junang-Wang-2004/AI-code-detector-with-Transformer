class C1(object):

    def makeFancyString(self, a1):
        """
        """
        a1 = list(a1)
        v2 = v3 = 0
        for v4, v5 in enumerate(a1):
            v2 = v2 + 1 if v4 >= 1 and v5 == a1[v4 - 1] else 1
            if v2 < 3:
                a1[v3] = v5
                v3 += 1
        a1[:] = a1[:v3]
        return ''.join(a1)
