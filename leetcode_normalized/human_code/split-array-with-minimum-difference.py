class C1(object):

    def splitArray(self, a1):
        """
        """
        v1, v2 = (0, 0)
        while v2 + 1 < len(a1) and a1[v2] < a1[v2 + 1]:
            v1 += a1[v2]
            v2 += 1
        v3, v4 = (0, len(a1) - 1)
        while v4 - 1 >= 0 and a1[v4] < a1[v4 - 1]:
            v3 += a1[v4]
            v4 -= 1
        if v4 - v2 + 1 >= 3:
            return -1
        if v4 - v2 + 1 == 2:
            return abs(v3 + a1[v4] - (v1 + a1[v2]))
        return min(abs(v3 - (v1 + a1[v2])), abs(v3 + a1[v4] - v1))
