class C1(object):

    def digArtifacts(self, a1, a2, a3):
        """
        """
        v1 = set(map(tuple, a3))
        return sum((all(((i, j) in v1 for v2 in range(r1, r2 + 1) for v3 in range(c1, c2 + 1))) for v4, v5, v6, v7 in a2))
