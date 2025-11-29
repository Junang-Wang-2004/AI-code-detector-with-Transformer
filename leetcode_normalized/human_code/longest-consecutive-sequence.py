class C1(object):

    def longestConsecutive(self, a1):
        v1, v2 = (1, {key: 0 for v3 in a1})
        for v4 in a1:
            if v2[v4] == 0:
                v2[v4] = 1
                v5, v6 = (v2.get(v4 - 1, 0), v2.get(v4 + 1, 0))
                v7 = 1 + v5 + v6
                v1, v2[v4 - v5], v2[v4 + v6] = (max(v1, v7), v7, v7)
        return v1
