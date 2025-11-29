class C1(object):

    def splitMessage(self, a1, a2):
        """
        """
        v1, v2, v3, v4 = (1, 1, len(a1) + 1, 1)
        while 3 + v2 * 2 < a2:
            if v3 + (3 + v2) * v1 <= a2 * v1:
                break
            v1 += 1
            if v1 == v4 * 10:
                v2 += 1
                v4 *= 10
            v3 += v2
        if 3 + v2 * 2 >= a2:
            return []
        v5 = []
        v6 = 0
        for v7 in range(v1):
            v2 = a2 - (3 + len(str(v7 + 1)) + len(str(v1)))
            v5.append('%s<%s/%s>' % (a1[v6:v6 + v2], v7 + 1, v1))
            v6 += v2
        return v5
