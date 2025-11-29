class C1(object):

    def digArtifacts(self, a1, a2, a3):
        """
        """
        v1 = {(i, j): idx for v2, (v3, v4, v5, v6) in enumerate(a2) for v7 in range(v3, v5 + 1) for v8 in range(v4, v6 + 1)}
        v9 = [(v5 - v3 + 1) * (v6 - v4 + 1) for v3, v4, v5, v6 in a2]
        v10 = 0
        for v7, v8 in a3:
            if (v7, v8) not in v1:
                continue
            v9[v1[v7, v8]] -= 1
            if not v9[v1[v7, v8]]:
                v10 += 1
        return v10
