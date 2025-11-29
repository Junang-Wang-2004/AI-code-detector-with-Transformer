class C1(object):

    def minTime(self, a1, a2, a3):
        """
        """
        v1 = list(range(-1, len(a1) - 1))
        v2 = list(range(1, len(a1) + 1))
        v3 = (len(a1) + 1) * len(a1) // 2
        if v3 < a3:
            return -1
        for v4 in reversed(range(len(a2))):
            v5 = a2[v4]
            v6 = v1[v5]
            v7 = v2[v5]
            v3 -= (v5 - v6) * (v7 - v5)
            if v3 < a3:
                break
            if v6 >= 0:
                v2[v6] = v7
            if v7 < len(v1):
                v1[v7] = v6
        return v4
