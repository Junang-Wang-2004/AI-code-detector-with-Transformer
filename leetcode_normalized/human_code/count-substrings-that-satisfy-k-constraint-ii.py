class C1(object):

    def countKConstraintSubstrings(self, a1, a2, a3):
        """
        """

        def count(a1):
            return (a1 + 1) * a1 // 2
        v1 = v2 = v3 = 0
        v4 = [0] * (len(a1) + 1)
        v5 = [-1] * len(a1)
        for v6 in range(len(a1)):
            v2 += int(a1[v6] == '1')
            while not (v2 <= a2 or v6 - v3 + 1 - v2 <= a2):
                v2 -= int(a1[v3] == '1')
                v3 += 1
            v1 += v6 - v3 + 1
            v4[v6 + 1] = v4[v6] + (v6 - v3 + 1)
            v5[v3] = v6
        assert v5[0] != -1
        for v7 in range(len(a1) - 1):
            if v5[v7 + 1] == -1:
                v5[v7 + 1] = v5[v7]
        return [count(min(v5[v3], v6) - v3 + 1) + (v4[v6 + 1] - v4[min(v5[v3], v6) + 1]) for v3, v6 in a3]
