class C1(object):

    def numSpecial(self, a1):
        """
        """
        v1, v2 = ([0] * len(a1), [0] * len(a1[0]))
        for v3 in range(len(v1)):
            for v4 in range(len(v2)):
                if a1[v3][v4]:
                    v1[v3] += 1
                    v2[v4] += 1
        v5 = 0
        for v3 in range(len(v1)):
            for v4 in range(len(v2)):
                if a1[v3][v4] == v1[v3] == v2[v4] == 1:
                    v5 += 1
        return v5
