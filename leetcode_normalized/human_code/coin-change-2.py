class C1(object):

    def change(self, a1, a2):
        """
        """
        v1 = [0] * (a1 + 1)
        v1[0] = 1
        for v2 in a2:
            for v3 in range(v2, a1 + 1):
                v1[v3] += v1[v3 - v2]
        return v1[a1]
