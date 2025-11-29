class C1(object):

    def minimalKSum(self, a1, a2):
        """
        """
        v1 = a2 * (a2 + 1) // 2
        v2 = a2 + 1
        for v3 in sorted(set(a1)):
            if v3 < v2:
                v1 += v2 - v3
                v2 += 1
        return v1
