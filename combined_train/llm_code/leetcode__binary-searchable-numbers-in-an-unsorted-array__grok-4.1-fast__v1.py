class C1(object):

    def binarySearchableNumbers(self, a1):
        v1 = len(a1)
        v2 = [float('-inf')] * v1
        if v1 > 0:
            v2[0] = a1[0]
            for v3 in range(1, v1):
                v2[v3] = max(v2[v3 - 1], a1[v3])
        v4 = [float('inf')] * v1
        if v1 > 0:
            v4[v1 - 1] = a1[v1 - 1]
            for v3 in range(v1 - 2, -1, -1):
                v4[v3] = min(v4[v3 + 1], a1[v3])
        v5 = set()
        for v3 in range(v1):
            v6 = float('-inf') if v3 == 0 else v2[v3 - 1]
            v7 = float('inf') if v3 == v1 - 1 else v4[v3 + 1]
            if v6 <= a1[v3] <= v7:
                v5.add(a1[v3])
        return len(v5)
