class C1(object):

    def largestGoodInteger(self, a1):
        """
        """
        v1 = ''
        v2 = 0
        for v3, v4 in enumerate(a1):
            v2 += 1
            if v3 + 1 < len(a1) and a1[v3] == a1[v3 + 1]:
                continue
            if v2 >= 3:
                v1 = max(v1, a1[v3])
            v2 = 0
        return v1 * 3
