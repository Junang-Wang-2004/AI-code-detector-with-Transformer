class C1:

    def resultsArray(self, a1, a2):
        v1 = len(a1)
        v2 = [-1] * (v1 - a2 + 1)
        v3 = 0
        while v3 < v1:
            v4 = v3
            while v4 + 1 < v1 and a1[v4 + 1] == a1[v4] + 1:
                v4 += 1
            v5 = v4 - v3 + 1
            if v5 >= a2:
                for v6 in range(v3, v4 - a2 + 2):
                    v2[v6] = a1[v6 + a2 - 1]
            v3 = v4 + 1
        return v2
