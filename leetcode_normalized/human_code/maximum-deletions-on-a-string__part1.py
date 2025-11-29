class C1(object):

    def deleteString(self, a1):
        """
        """
        if all((x == a1[0] for v1 in a1)):
            return len(a1)
        v2 = [[0] * (len(a1) + 1) for v3 in range(2)]
        v4 = [1] * len(a1)
        for v3 in reversed(range(len(a1) - 1)):
            for v5 in range(v3 + 1, len(a1)):
                v2[v3 % 2][v5] = v2[(v3 + 1) % 2][v5 + 1] + 1 if a1[v5] == a1[v3] else 0
                if v2[v3 % 2][v5] >= v5 - v3:
                    v4[v3] = max(v4[v3], v4[v5] + 1)
        return v4[0]
