class C1(object):

    def probabilityOfHeads(self, a1, a2):
        """
        """
        v1 = [0.0] * (a2 + 1)
        v1[0] = 1.0
        for v2 in a1:
            for v3 in reversed(range(a2 + 1)):
                v1[v3] = (v1[v3 - 1] if v3 >= 1 else 0.0) * v2 + v1[v3] * (1 - v2)
        return v1[a2]
