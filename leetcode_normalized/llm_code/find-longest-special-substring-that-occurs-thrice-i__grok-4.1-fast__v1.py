class C1(object):

    def maximumLength(self, a1):
        v1 = [[] for v2 in range(26)]
        v3 = len(a1)
        v4 = 0
        while v4 < v3:
            v5 = a1[v4]
            v6 = v4
            while v4 < v3 and a1[v4] == v5:
                v4 += 1
            v1[ord(v5) - ord('a')].append(v4 - v6)
        v7 = 0
        for v8 in v1:
            if not v8:
                continue
            v8.sort(reverse=True)
            v7 = max(v7, v8[0] - 2)
            v9 = len(v8)
            if v9 >= 2:
                v7 = max(v7, min(v8[0] - 1, v8[1]))
            if v9 >= 3:
                v7 = max(v7, v8[2])
        return v7 if v7 > 0 else -1
