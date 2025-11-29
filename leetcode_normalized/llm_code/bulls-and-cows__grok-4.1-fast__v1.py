class C1:

    def getHint(self, a1, a2):
        v1 = 0
        v2 = [0] * 10
        v3 = [0] * 10
        v4 = len(a1)
        for v5 in range(v4):
            v6 = ord(a1[v5]) - ord('0')
            v7 = ord(a2[v5]) - ord('0')
            if v6 == v7:
                v1 += 1
            else:
                v2[v6] += 1
                v3[v7] += 1
        v8 = sum((min(v2[j], v3[j]) for v9 in range(10)))
        return f'{v1}A{v8}B'
