class C1:

    def numberOfWeakCharacters(self, a1):
        a1.sort(key=lambda x: -x[0])
        v1 = 0
        v2 = 0
        v3 = 0
        v4 = len(a1)
        while v3 < v4:
            v5 = a1[v3][0]
            v6 = 0
            v7 = 0
            while v3 < v4 and a1[v3][0] == v5:
                v8 = a1[v3][1]
                if v8 < v2:
                    v6 += 1
                v7 = max(v7, v8)
                v3 += 1
            v1 += v6
            v2 = max(v2, v7)
        return v1
