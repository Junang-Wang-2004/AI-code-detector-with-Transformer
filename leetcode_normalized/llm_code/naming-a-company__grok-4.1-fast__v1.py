class C1(object):

    def distinctNames(self, a1):
        v1 = [set() for v2 in range(26)]
        for v3 in a1:
            v4 = ord(v3[0]) - ord('a')
            v1[v4].add(v3[1:])
        v5 = 0
        for v6 in range(26):
            for v7 in range(26):
                if v6 == v7:
                    continue
                v8 = len(v1[v6] & v1[v7])
                v9 = len(v1[v6]) - v8
                v10 = len(v1[v7]) - v8
                v5 += v9 * v10
        return v5
