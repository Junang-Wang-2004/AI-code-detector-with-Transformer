class C1(object):

    def largestPathValue(self, a1, a2):
        v1 = len(a1)
        v2 = [[] for v3 in range(v1)]
        for v4, v5 in a2:
            v2[v4].append(v5)
        v6 = [None] * v1
        v7 = [False] * v1
        v8 = False
        v9 = 0

        def get_maxes(a1):
            nonlocal cycle_exists, best
            if v6[a1] is not None:
                return v6[a1]
            if v7[a1]:
                v1 = True
                return [0] * 26
            v7[a1] = True
            v2 = ord(a1[a1]) - ord('a')
            v3 = [0] * 26
            for v4 in v2[a1]:
                v5 = get_maxes(v4)
                for v6 in range(26):
                    v3[v6] = max(v3[v6], v5[v6])
            v7 = [(1 if v6 == v2 else 0) + v3[v6] for v6 in range(26)]
            v7[a1] = False
            v6[a1] = v7
            v8 = max(v8, max(v7))
            return v7
        for v10 in range(v1):
            if v6[v10] is None:
                get_maxes(v10)
        return -1 if v8 else v9
