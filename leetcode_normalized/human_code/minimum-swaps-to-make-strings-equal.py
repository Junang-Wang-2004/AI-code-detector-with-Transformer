class C1(object):

    def minimumSwap(self, a1, a2):
        """
        """
        v1, v2 = (0, 0)
        for v3 in range(len(a1)):
            if a1[v3] == a2[v3]:
                continue
            v1 += int(a1[v3] == 'x')
            v2 += int(a1[v3] == 'y')
        if v1 % 2 != v2 % 2:
            return -1
        return v1 // 2 + v2 // 2 + (v1 % 2 + v2 % 2)
