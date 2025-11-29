class C1(object):

    def minimumOperations(self, a1):
        """
        """
        v1 = 0
        v2, v3 = (0, len(a1) - 1)
        v4, v5 = (a1[v2], a1[v3])
        while v2 < v3:
            if v4 == v5:
                v2 += 1
                v3 -= 1
                v4, v5 = (a1[v2], a1[v3])
                continue
            if v4 < v5:
                v2 += 1
                v4 += a1[v2]
            else:
                v3 -= 1
                v5 += a1[v3]
            v1 += 1
        return v1
