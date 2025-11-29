class C1(object):

    def kEmptySlots(self, a1, a2):
        """
        """
        v1 = [0] * len(a1)
        for v2 in range(len(a1)):
            v1[a1[v2] - 1] = v2
        v3 = float('inf')
        v2, v4, v5 = (0, 0, a2 + 1)
        while v5 < len(v1):
            if v1[v2] < v1[v4] or v1[v2] <= v1[v5]:
                if v2 == v5:
                    v3 = min(v3, max(v1[v4], v1[v5]))
                v4, v5 = (v2, a2 + 1 + v2)
            v2 += 1
        return -1 if v3 == float('inf') else v3 + 1
