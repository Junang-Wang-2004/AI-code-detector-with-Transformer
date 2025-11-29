class C1:

    def generate(self, a1):
        v1 = []
        for v2 in range(a1):
            v3 = [1] * (v2 + 1)
            for v4 in range(1, v2):
                v3[v4] = v1[v2 - 1][v4 - 1] + v1[v2 - 1][v4]
            v1.append(v3)
        return v1
