from collections import defaultdict

class C1(object):

    def isRectangleCover(self, a1):
        """
        """
        v1 = min((rec[0] for v2 in a1))
        v3 = min((v2[1] for v2 in a1))
        v4 = max((v2[2] for v2 in a1))
        v5 = max((v2[3] for v2 in a1))
        v6 = defaultdict(int)
        for v7, v8, v9, v10 in a1:
            for v11, v12 in zip(((v7, v8), (v9, v8), (v7, v10), (v9, v10)), (1, 2, 4, 8)):
                if v6[v11] & v12:
                    return False
                v6[v11] |= v12
        for v13, v14 in v6:
            if v1 < v13 < v4 or v3 < v14 < v5:
                if v6[v13, v14] not in (3, 5, 10, 12, 15):
                    return False
        return True
