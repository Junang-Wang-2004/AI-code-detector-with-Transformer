class C1(object):

    def threeEqualParts(self, a1):
        """
        """
        v1 = sum(a1)
        if v1 % 3 != 0:
            return [-1, -1]
        if v1 == 0:
            return [0, len(a1) - 1]
        v2 = v1 // 3
        v3 = [0] * 3
        v4 = 0
        for v5 in range(len(a1)):
            if a1[v5] == 1:
                if v4 % v2 == 0:
                    v3[v4 // v2] = v5
                v4 += 1
        while v3[2] != len(a1):
            if not a1[v3[0]] == a1[v3[1]] == a1[v3[2]]:
                return [-1, -1]
            v3[0] += 1
            v3[1] += 1
            v3[2] += 1
        return [v3[0] - 1, v3[1]]
