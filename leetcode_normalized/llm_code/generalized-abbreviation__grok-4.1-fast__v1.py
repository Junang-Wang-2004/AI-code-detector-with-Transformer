class C1:

    def generateAbbreviations(self, a1):
        v1 = len(a1)
        v2 = []
        for v3 in range(1 << v1):
            v4 = [-1]
            for v5 in range(v1):
                if v3 & 1 << v5:
                    v4.append(v5)
            v4.append(v1)
            v6 = []
            for v7 in range(1, len(v4)):
                v8 = v4[v7 - 1]
                v9 = v4[v7]
                v10 = v9 - v8 - 1
                if v10 > 0:
                    v6.append(str(v10))
                if v9 < v1:
                    v6.append(a1[v9])
            v2.append(''.join(v6))
        return v2
