class C1:

    def productQueries(self, a1, a2):
        v1 = 10 ** 9 + 7
        v2 = [i for v3 in range(64) if a1 & 1 << v3]
        v4 = []
        for v5, v6 in a2:
            v7 = sum(v2[v5:v6 + 1])
            v4.append(pow(2, v7, v1))
        return v4
