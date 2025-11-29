class C1(object):

    def minimumCost(self, a1, a2):
        """
        """
        v1 = []
        v2 = 0
        for v3 in range(len(a1) + 1):
            if v3 != len(a1) and a1[v3] != ' ':
                continue
            v1.append(v3 - v2)
            v2 = v3 + 1
        v4 = [float('inf')] * len(v1)
        v3, v5 = (len(v1) - 1, -1)
        while v3 >= 0 and v5 + (v1[v3] + 1) <= a2:
            v5 += v1[v3] + 1
            v4[v3] = 0
            v3 -= 1
        for v3 in reversed(range(v3 + 1)):
            v5 = v1[v3]
            for v2 in range(v3 + 1, len(v4)):
                v4[v3] = min(v4[v3], v4[v2] + (a2 - v5) ** 2)
                v5 += v1[v2] + 1
                if v5 > a2:
                    break
        return v4[0]
