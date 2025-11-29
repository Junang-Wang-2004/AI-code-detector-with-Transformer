class C1(object):

    def maximumBinaryString(self, a1):
        """
        """
        v1 = list(a1)
        v2 = v3 = 0
        for v4, v5 in enumerate(v1):
            if v5 == '0':
                v2 += 1
            elif v2 == 0:
                v3 += 1
            v1[v4] = '1'
        if v3 != len(v1):
            v1[v2 + v3 - 1] = '0'
        return ''.join(v1)
