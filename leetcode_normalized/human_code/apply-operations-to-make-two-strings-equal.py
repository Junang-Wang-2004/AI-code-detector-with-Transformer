class C1(object):

    def minOperations(self, a1, a2, a3):
        """
        """
        v1 = v2 = v3 = 0
        v4 = -1
        for v5 in range(len(a1)):
            if a1[v5] == a2[v5]:
                continue
            v2, v3 = (min(v2 + a3, v3 + (v5 - v4) * 2 if v4 != -1 else float('inf')), v2)
            v4 = v5
            v1 ^= 1
        return v2 // 2 if v1 == 0 else -1
