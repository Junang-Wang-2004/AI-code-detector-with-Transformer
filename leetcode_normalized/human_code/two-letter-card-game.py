class C1(object):

    def score(self, a1, a2):
        v1 = [0] * 26
        v2 = [0] * 26
        v3 = 0
        for v4 in a1:
            if a2 not in v4:
                continue
            if v4[0] == a2 == v4[1]:
                v3 += 1
            elif v4[0] == a2:
                v1[ord(v4[1]) - ord('a')] += 1
            elif v4[1] == a2:
                v2[ord(v4[0]) - ord('a')] += 1
        v5, v6 = (sum(v1), sum(v2))
        v7, v8 = (max(v1), max(v2))
        v9, v10 = (min(v5 - v7, v5 // 2), min(v6 - v8, v6 // 2))
        v11 = min(v5 - 2 * v9 + (v6 - 2 * v10), v3)
        return v9 + v10 + v11 + min(v9 + v10, (v3 - v11) // 2)
