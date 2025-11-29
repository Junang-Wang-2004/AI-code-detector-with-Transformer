class C1(object):

    def multiply(self, a1, a2):
        """
        """
        v1, v2, v3 = (len(a1), len(a1[0]), len(a2[0]))
        v4 = [[0 for v5 in range(v3)] for v5 in range(v1)]
        for v6 in range(v1):
            for v7 in range(v2):
                if a1[v6][v7]:
                    for v8 in range(v3):
                        v4[v6][v8] += a1[v6][v7] * a2[v7][v8]
        return v4
