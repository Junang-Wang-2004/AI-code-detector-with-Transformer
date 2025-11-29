class C1(object):

    def resultArray(self, a1, a2):
        """
        """
        v1 = [0] * a2
        v2 = [0] * a2
        for v3 in a1:
            v4 = [0] * a2
            v4[v3 % a2] += 1
            for v5, v6 in enumerate(v2):
                v4[v5 * v3 % a2] += v6
            for v5, v6 in enumerate(v4):
                v1[v5] += v6
            v2 = v4
        return v1
