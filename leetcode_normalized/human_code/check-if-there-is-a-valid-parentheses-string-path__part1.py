class C1(object):

    def hasValidPath(self, a1):
        """
        """
        if (len(a1) + len(a1[0]) - 1) % 2:
            return False
        v1 = [0] * (len(a1[0]) + 1)
        for v2 in range(len(a1)):
            v1[0] = int(not v2)
            for v3 in range(len(a1[0])):
                v1[v3 + 1] = (v1[v3] | v1[v3 + 1]) << 1 if a1[v2][v3] == '(' else (v1[v3] | v1[v3 + 1]) >> 1
        return v1[-1] & 1
