class C1:

    def compress(self, a1):
        v1 = 0
        v2 = 0
        v3 = len(a1)
        while v2 < v3:
            v4 = v2
            while v4 < v3 and a1[v4] == a1[v2]:
                v4 += 1
            a1[v1] = a1[v2]
            v1 += 1
            v5 = v4 - v2
            if v5 > 1:
                for v6 in str(v5):
                    a1[v1] = v6
                    v1 += 1
            v2 = v4
        return v1
