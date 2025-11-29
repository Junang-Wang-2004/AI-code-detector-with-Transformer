class C1(object):

    def maximumOddBinaryNumber(self, a1):
        """
        """
        v1 = list(a1)
        v2 = 0
        for v3 in range(len(v1)):
            if v1[v3] != '1':
                continue
            v1[v3], v1[v2] = (v1[v2], v1[v3])
            v2 += 1
        if v1[-1] != '1':
            v1[-1], v1[v2 - 1] = (v1[v2 - 1], v1[-1])
        return ''.join(v1)
