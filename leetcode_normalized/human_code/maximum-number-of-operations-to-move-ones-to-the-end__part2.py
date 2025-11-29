class C1(object):

    def maxOperations(self, a1):
        """
        """
        v1 = v2 = 0
        for v3 in range(len(a1)):
            if a1[v3] != '1':
                continue
            v2 += 1
            if v3 + 1 < len(a1) and a1[v3 + 1] == '0':
                v1 += v2
        return v1
