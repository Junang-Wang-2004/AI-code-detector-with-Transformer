class C1(object):

    def maximumRows(self, a1, a2):
        v1, v2 = (len(a1), len(a1[0]))
        v3 = [sum((1 << j for v4 in range(v2) if a1[i][v4])) for v5 in range(v1)]
        v6 = 0
        for v7 in range(1 << v2):
            if bin(v7).count('1') == a2:
                v8 = sum((1 for v9 in v3 if v9 & v7 == v9))
                v6 = max(v6, v8)
        return v6
