class C1:

    def rotate(self, a1, a2):
        v1 = len(a1)
        v2 = a2 % v1
        for v3 in range(v1 // 2):
            a1[v3], a1[v1 - 1 - v3] = (a1[v1 - 1 - v3], a1[v3])
        for v3 in range(v2 // 2):
            a1[v3], a1[v2 - 1 - v3] = (a1[v2 - 1 - v3], a1[v3])
        v4 = v1 - v2
        for v3 in range(v4 // 2):
            a1[v2 + v3], a1[v1 - 1 - v3] = (a1[v1 - 1 - v3], a1[v2 + v3])
