class C1(object):

    def convert(self, a1, a2):
        """
        """
        if a2 == 1:
            return a1
        v1, v2 = (2 * a2 - 2, '')
        for v3 in range(a2):
            for v4 in range(v3, len(a1), v1):
                v2 += a1[v4]
                if 0 < v3 < a2 - 1 and v4 + v1 - 2 * v3 < len(a1):
                    v2 += a1[v4 + v1 - 2 * v3]
        return v2
