class C1(object):

    def numDecodings(self, a1):
        """
        """
        if len(a1) == 0 or a1[0] == '0':
            return 0
        v1, v2 = (1, 0)
        for v3 in range(len(a1)):
            v4 = 0
            if a1[v3] != '0':
                v4 = v1
            if v3 > 0 and (a1[v3 - 1] == '1' or (a1[v3 - 1] == '2' and a1[v3] <= '6')):
                v4 += v2
            v1, v2 = (v4, v1)
        return v1
