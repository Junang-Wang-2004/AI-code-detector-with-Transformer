class C1(object):

    def hasAllCodes(self, a1, a2):
        """
        """
        v1 = set()
        v2 = 2 ** a2
        if v2 > len(a1):
            return False
        v3 = 0
        for v4 in range(len(a1)):
            v3 = (v3 << 1) + (a1[v4] == '1')
            if v4 >= a2 - 1:
                v1.add(v3)
                v3 -= (a1[v4 - a2 + 1] == '1') * (v2 // 2)
        return len(v1) == v2
