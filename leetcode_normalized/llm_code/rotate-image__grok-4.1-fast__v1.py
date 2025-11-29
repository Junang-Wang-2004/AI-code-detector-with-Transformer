class C1:

    def rotate(self, a1):
        v1 = len(a1)
        for v2 in range(v1):
            for v3 in range(v2 + 1, v1):
                a1[v2][v3], a1[v3][v2] = (a1[v3][v2], a1[v2][v3])
        for v4 in range(v1):
            a1[v4].reverse()
        return a1
