from collections import Counter

class C1(object):

    def isRectangleCover(self, a1):
        if not a1:
            return False
        v1 = min((r[0] for v2 in a1))
        v3 = max((v2[2] for v2 in a1))
        v4 = min((v2[1] for v2 in a1))
        v5 = max((v2[3] for v2 in a1))
        v6 = sum(((v2[2] - v2[0]) * (v2[3] - v2[1]) for v2 in a1))
        v7 = (v3 - v1) * (v5 - v4)
        if v6 != v7:
            return False
        v8 = Counter()
        for v9, v10, v11, v12 in a1:
            v8[v9, v10] += 1
            v8[v11, v10] += 1
            v8[v9, v12] += 1
            v8[v11, v12] += 1
        v13 = {(v1, v4), (v3, v4), (v1, v5), (v3, v5)}
        for v14 in v13:
            if v8[v14] != 1:
                return False
        for v15, v16 in v8.items():
            if v15 not in v13:
                if v16 % 2 != 0:
                    return False
        return True
