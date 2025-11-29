class C1(object):

    def rotate(self, a1):
        v1 = len(a1)
        for v2 in range(v1):
            for v3 in range(v1 - v2):
                a1[v2][v3], a1[v1 - 1 - v3][v1 - 1 - v2] = (a1[v1 - 1 - v3][v1 - 1 - v2], a1[v2][v3])
        for v2 in range(v1 / 2):
            for v3 in range(v1):
                a1[v2][v3], a1[v1 - 1 - v2][v3] = (a1[v1 - 1 - v2][v3], a1[v2][v3])
        return a1
